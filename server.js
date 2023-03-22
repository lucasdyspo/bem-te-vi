// Webpack dev server
import webpack from 'webpack';
import WebpackDevServer from 'webpack-dev-server';

import baseConfig from './webpack.local.config.cjs';

new WebpackDevServer(webpack(baseConfig), {
  publicPath: baseConfig.output.publicPath,
  port: 3000,
  hot: true,
  inline: true,
  historyApiFallback: true,
  headers: { 'Access-Control-Allow-Origin': '*' },
}).listen(3000, '0.0.0.0', (err) => {
  if (err) {
    console.log(err);
  }

  console.log('Listening at 0.0.0.0:3000');
});
