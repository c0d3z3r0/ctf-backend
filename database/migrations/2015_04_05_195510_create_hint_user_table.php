<?php

use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Migrations\Migration;

class CreateHintUserTable extends Migration {

	/**
	 * Run the migrations.
	 *
	 * @return void
	 */
	public function up()
	{
		Schema::create('hint_user', function(Blueprint $table)
		{
			$table->engine = 'InnoDB';

			$table->integer('user_id')->unsigned();
			$table->integer('hint_id')->unsigned();
			$table->timestamps();

			$table->primary(['user_id', 'hint_id']);
			$table->foreign('user_id')
						->references('id')->on('users')
						->onDelete('cascade');
			$table->foreign('hint_id')
						->references('id')->on('hints')
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
		Schema::drop('hint_user');
	}

}
