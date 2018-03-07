const path = require('path');
const webpack = require("webpack");
const ExtractTextPlugin = require("extract-text-webpack-plugin");
const LiveReloadPlugin = require('webpack-livereload-plugin');

const extractLess = new ExtractTextPlugin({
    filename: "styles.css",
});

const Static = './personalsite/static/'
const JsDir = Static + 'js/'


module.exports = {	
  entry: {
    bundle: JsDir + 'index.js'
    // temporarily taken out of use
    // app: JsDir + 'app.js',
  },
  output: {
    filename: '[name].js',
    path: path.resolve(__dirname, Static + 'dist')
  },
  module: {
      rules: [{
          test: /\.less$/,
          use: extractLess.extract({
              use: [{
                  loader: "css-loader"
              }, {
                  loader: "less-loader"
              }],

          })
        },
        {
          // not in use yet
          test: /\.js$/,
          exclude: /node_modules/,
          use: {
            loader: "babel-loader"
          }
        },
        {
          // not in use yet
          test: /\.html$/,
          use: [
            {
              loader: "html-loader"
            }
          ]
        }]
  },
  plugins: [
      extractLess,
      new LiveReloadPlugin()
  ]

};
