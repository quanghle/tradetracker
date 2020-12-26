const HOSTNAME = process.env.HOSTNAME || 'localhost';

const PROXY_CONFIG = {
  "/graphql": {
      "target": `http://${HOSTNAME}:8000`,
      "secure": false
  }
}

module.exports = PROXY_CONFIG;