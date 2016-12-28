var debug = process.env.NODE_ENV !== "production";
var webpack = require('webpack');
var path = require('path');

module.exports = {
  context: __dirname,
  devtool: debug ? "inline-sourcemap" : null,
  entry: {
    layout_main: "./layout/js/index.js",
    clients_addEdit: "./common/clients/js/addEdit/index.js",
    products_main: "./common/products/js/lib/list/index.js",
    products_addEdit: "./common/products/js/lib/create/index.js",
    pos_main: "./sales/poss/js/index.js",
  },
  module:{
    loaders: [
      {
        test: /\.jsx?$/,
        exclude: /(node_modules|bower_components)/,
        loader: 'babel-loader',
        query: {
          presets: ["es2015", "stage-0"],
        }
      }
    ],
  },
  output: {

    path: __dirname + "/public/js/",
    filename: "[name].js"
  },

  plugins: debug ? [] : [
    new webpack.optimize.DedupePlugin(),
    new webpack.optimize.OccurenceOrderPlugin(),
    new webpack.optimize.UglifyJsPlugin({ mangle: false, sourcemap: false }),
  ],

};
