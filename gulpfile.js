var gulp = require('gulp');
var addsrc = require('gulp-add-src');
var plumber = require('gulp-plumber');
var concat = require("gulp-concat");
var less = require('gulp-less');
var rollup = require('rollup').rollup;
var buble = require('rollup-plugin-buble');
var resolve = require('rollup-plugin-node-resolve');
var commonjs = require('rollup-plugin-commonjs');

var build_tasks = ['build-js', 'build-css'];

gulp.task('build-js', function () {
  // including vue externally so it builds faster
  return rollup({
    input: './static/coda/main.js',
    plugins: [
      resolve({ jsnext: true }),
      commonjs(),
      buble({transforms: { forOf: false }})
    ],
    external: ['axios', 'vue', 'vue-router', 'vue-material', 'vuex']
  }).then(function (bundle) {
    return bundle.write({
      format: 'iife',
      file: './static/dist/main.js',
      globals: {
        "vue": 'Vue',
        "vue-router": 'VueRouter',
        "vue-material": 'VueMaterial',
        "vuex": 'Vuex'
      },
    });
  });
});

gulp.task('build-css', function () {
  return gulp.src("static/coda/**/*.less")
    .pipe(plumber())
    .pipe(less({paths: ['static/less']}))
    .pipe(addsrc('node_modules/vue-material/dist/vue-material.css'))
    .pipe(concat('coda.css'))
    .pipe(gulp.dest("static/dist"));
});

gulp.task('watch', build_tasks, function () {
  gulp.watch("static/coda/**/*.js", ['build-js']);
  gulp.watch("static/**/*.less", ['build-css']);
});

gulp.task('default', build_tasks);

