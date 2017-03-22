var debug = process.env.NODE_ENV !== "production";
var webpack = require('webpack');
var path = require('path');

module.exports = {
  context: __dirname,
  devtool: debug ? "inline-sourcemap" : null,
  entry: {
    layout_main: "./layout/js/index.js",
    clients_addEdit: "./sales/clients/js/addEdit/index.js",
    products_main: "./sales/products/js/lib/list/index.js",
    products_addEdit: "./sales/products/js/lib/create/index.js",
    entries_addEdit: "./accounting/entries/js/lib/create/index.js",
    catalog_list: "./accounting/catalog/js/lib/list/index.js",
    catalog_addEdit: "./accounting/catalog/js/lib/create/index.js",
    report: "./accounting/reports/js/index.js",
    pos_main: "./sales/pos/js/index.js",
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
