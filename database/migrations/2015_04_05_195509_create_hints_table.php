<?php

use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Migrations\Migration;

class CreateHintsTable extends Migration {

	/**
	 * Run the migrations.
	 *
	 * @return void
	 */
	public function up()
	{
		Schema::create('hints', function(Blueprint $table)
		{
			$table->engine = 'InnoDB';

			$table->increments('id');
			$table->integer('challenge_id')->unsigned()->index();
			$table->string('name', 50);
			$table->text('description');
			$table->integer('price')->unsigned();
			$table->timestamps();

			$table->foreign('challenge_id')
      			->references('id')->on('challenges')
      			->onDelete('cascade');
		});
	}

	/**
	 * Reverse the migrations.
	 *
	 * @return void
	 */
	public function down()
	{
		Schema::drop('hints');
	}

}
