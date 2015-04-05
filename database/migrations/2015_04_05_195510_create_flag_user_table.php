<?php

use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Migrations\Migration;

class CreateFlagUserTable extends Migration {

	/**
	 * Run the migrations.
	 *
	 * @return void
	 */
	public function up()
	{
		Schema::create('flag_user', function(Blueprint $table)
		{
			$table->engine = 'InnoDB';

			$table->integer('user_id')->unsigned();
			$table->integer('flag_id')->unsigned();
			$table->text('solution');
			$table->timestamps();

			$table->primary(['user_id', 'flag_id']);
			$table->foreign('user_id')
						->references('id')->on('users')
						->onDelete('cascade');
			$table->foreign('flag_id')
						->references('id')->on('flags')
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
		Schema::drop('flag_user');
	}

}
