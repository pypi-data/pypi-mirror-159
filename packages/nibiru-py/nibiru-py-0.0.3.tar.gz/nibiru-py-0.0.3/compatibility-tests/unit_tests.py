import pytest
import aiohttp
import json
import ecdsa
import sha3
import grpc
import base64

from typing import Any, Dict, List
from nibiru.chain_client._wallet import (
    generate_wallet,
    privkey_to_address,
    privkey_to_pubkey,
    pubkey_to_address,
    seed_to_privkey,
    DEFAULT_BECH32_HRP,
)

from nibiru.chain_client._typings import SyncMode
import nibiru.exchange_api.nibiru_accounts_rpc_pb2 as accounts_rpc_pb
import nibiru.exchange_api.nibiru_accounts_rpc_pb2_grpc as accounts_rpc_grpc

MIN_GAS_PRICE = 500000000

class Transaction:

    def __init__(
        self,
        *,
        privkey: bytes,
        account_num: int,
        sequence: int,
        fee: int,
        gas: int,
        fee_denom: str = "inj",
        memo: str = "",
        chain_id: str = "nibiru-888",
        hrp: str = DEFAULT_BECH32_HRP,
        sync_mode: SyncMode = "block",
    ) -> None:
        self._privkey = privkey
        self._account_num = account_num
        self._sequence = sequence
        self._fee = fee
        self._fee_denom = fee_denom
        self._gas = gas
        self._memo = memo
        self._chain_id = chain_id
        self._hrp = hrp
        self._sync_mode = sync_mode
        self._msgs: List[dict] = []


    def add_cosmos_bank_msg_send(self, recipient: str, amount: int, denom: str = "inj") -> None:
        msg = {
            "type": "cosmos-sdk/MsgSend",
            "value": {
                "from_address": privkey_to_address(self._privkey, hrp=self._hrp),
                "to_address": recipient,
                "amount": [{"denom": denom, "amount": str(amount)}],
            },
        }
        self._msgs.append(msg)

    # Nibiru Exchange Module

    def add_exchange_msg_deposit(self, subaccount: str, amount: int, denom: str = "inj") -> None:
        msg = {
            "type": "exchange/MsgDeposit",
            "value": {
                "sender": privkey_to_address(self._privkey, hrp=self._hrp),
                "subaccount_id": subaccount,
                "amount": {"denom": denom, "amount": str(amount)},
            },
        }
        self._msgs.append(msg)

    def get_signed(self) -> str:
        pubkey = privkey_to_pubkey(self._privkey)
        base64_pubkey = base64.b64encode(pubkey).decode("utf-8")
        signed_tx = {
            "tx": {
                "msg": self._msgs,
                "fee": {
                    "gas": str(self._gas),
                    "amount": [{"denom": self._fee_denom, "amount": str(self._fee)}],
                },
                "memo": self._memo,
                "signatures": [
                    {
                        "signature": self._sign(),
                        "pub_key": {"type": "nibiru/PubKeyEthSecp256k1", "value": base64_pubkey},
                        "account_number": str(self._account_num),
                        "sequence": str(self._sequence),
                    }
                ],
            },
            "mode": self._sync_mode,
        }
        return json.dumps(signed_tx, separators=(",", ":"))

    def _sign(self) -> str:
        message_str = json.dumps(
            self._get_sign_message(), separators=(",", ":"), sort_keys=True)
        message_bytes = message_str.encode("utf-8")

        privkey = ecdsa.SigningKey.from_string(
            self._privkey, curve=ecdsa.SECP256k1)
        signature_compact_keccak = privkey.sign_deterministic(
            message_bytes, hashfunc=sha3.keccak_256, sigencode=ecdsa.util.sigencode_string_canonize
        )
        signature_base64_str = base64.b64encode(
            signature_compact_keccak).decode("utf-8")
        return signature_base64_str

    def _get_sign_message(self) -> Dict[str, Any]:
        return {
            "chain_id": self._chain_id,
            "account_number": str(self._account_num),
            "fee": {
                "gas": str(self._gas),
                "amount": [{"amount": str(self._fee), "denom": self._fee_denom}],
            },
            "memo": self._memo,
            "sequence": str(self._sequence),
            "msgs": self._msgs,
        }


async def get_account_num_seq(address: str) -> (int, int):
    async with aiohttp.ClientSession() as session:
        async with session.request(
            'GET', 'http://staking-lcd-testnet.nibiru.network/cosmos/auth/v1beta1/accounts/' + address,
            headers={'Accept-Encoding': 'application/json'},
        ) as response:
            if response.status != 200:
                print(await response.text())
                raise ValueError("HTTP response status", response.status)

            resp = json.loads(await response.text())
            acc = resp['account']['base_account']
            return acc['account_number'], acc['sequence']

async def post_tx(tx_json: str):
    async with aiohttp.ClientSession() as session:
        async with session.request(
            'POST', 'http://staking-lcd-testnet.nibiru.network/txs', data=tx_json,
            headers={'Content-Type': 'application/json'},
        ) as response:
            if response.status != 200:
                print(await response.text())
                raise ValueError("HTTP response status", response.status)

            resp = json.loads(await response.text())
            if 'code' in resp:
                print("Response:", resp)
                raise ValueError('sdk error %d: %s' % (resp['code'], resp['raw_log']))

            return resp['txhash']

@pytest.fixture
async def msg_send():
    sender_pk = seed_to_privkey(
        "physical page glare junk return scale subject river token door mirror title"
    )
    sender_acc_addr = privkey_to_address(sender_pk)
    print("Sender Account:", sender_acc_addr)

    acc_num, acc_seq = await get_account_num_seq(sender_acc_addr)

    async with grpc.aio.insecure_channel('testnet-sentry0.nibiru.network:9910') as channel:
        accounts_rpc = accounts_rpc_grpc.nibiruAccountsRPCStub(channel)
        account_addr = "inj14au322k9munkmx5wrchz9q30juf5wjgz2cfqku"

        subacc = await accounts_rpc.SubaccountsList(accounts_rpc_pb.SubaccountsListRequest(account_address = account_addr))
        for sub in subacc.subaccounts:
            print("Primary subaccount:", sub)
            break

    tx = Transaction(
        privkey=sender_pk,
        account_num=acc_num,
        sequence=acc_seq,
        gas=200000,
        fee=200000 * MIN_GAS_PRICE,
        sync_mode="block",
    )
    tx.add_cosmos_bank_msg_send(
        recipient="inj1qy69k458ppmj45c3vqwcd6wvlcuvk23x0hsz58",
        amount=10000000000000000,
        denom="inj",
    )
    tx.add_exchange_msg_deposit(
        subaccount= sub,
        amount=10000000000000000,
        denom="inj",
    )

    tx_json = tx.get_signed()
    tx_result = await post_tx(tx_json)

    print("Signed Tx:", tx_json)
    print("Sent Tx:", tx_result)

    return len(tx_result)

@pytest.mark.asyncio
async def test_msg_send(msg_send):
    assert msg_send == 64