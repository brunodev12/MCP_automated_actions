const TronWeb = require('tronweb');

async function signMessage(_message) {
  const tronWeb = new TronWeb(
    'https://api.trongrid.io',
    'https://api.trongrid.io',
    'https://api.trongrid.io'
    );

  var privateKey = process.env.PRIVATE_KEY_TRON;
  var message = _message;
  var HexStr = tronWeb.toHex(message);

  var signature = await tronWeb.trx.sign(HexStr, privateKey);
  console.log(signature);
}

signMessage(process.argv[2]);