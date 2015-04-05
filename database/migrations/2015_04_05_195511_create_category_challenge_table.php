<?php

use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Migrations\Migration;

class CreateCategoryChallengeTable extends Migration {

	/**
	 * Run the migrations.
	 *
	 * @return void
	 */
	public function up()
	{
		Schema::create('category_challenge', function(Blueprint $table)
		{
			$table->engine = 'InnoDB';

			$table->integer('challenge_id')->unsigned();
			$table->integer('category_id')->unsigned();
			$table->timestamps();

			$table->primary(['challenge_id', 'category_id']);
			$table->foreign('challenge_id')
						->references('id')->on('challenges')
						->onDelete('cascade');
			$table->foreign('category_id')
						->references('id')->on('categories')
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
		Schema::drop('category_challenge');
	}

}
