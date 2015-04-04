var elixir = require('laravel-elixir');

/*
 |--------------------------------------------------------------------------
 | Elixir Asset Management
 |--------------------------------------------------------------------------
 |
 | Elixir provides a clean, fluent API for defining some basic Gulp tasks
 | for your Laravel application. By default, we are compiling the Less
 | file for our application, as well as publishing vendor resources.
 |
 */

elixir(function(mix) {
    mix.less('app.less');

	mix.scripts([
		'../assets/bower/jquery/dist/jquery.js',
		'../assets/bower/bootstrap/dist/js/bootstrap.js',
		'../assets/bower/d3/d3.js',
		'../assets/bower/c3/c3.js',
		'custom.js'
    ]);

    mix.scripts([
		'../assets/bower/html5shiv/dist/html5shiv.js',
		'../assets/bower/respondJs/dest/respond.src.js'
	],	'public/js/ielt9.js');

    mix.styles([
		'../assets/bower/bootstrap/dist/css/bootstrap.css',
		'../assets/bower/c3/c3.css',
		'custom.css'
    ]);

	mix.version([
		'css/all.css',
		'js/all.js'
	]);

	mix.copy('resources/assets/bower/bootstrap/dist/fonts/**',
		'public/fonts');
});
