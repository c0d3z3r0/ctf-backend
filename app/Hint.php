<?php namespace App;

use Illuminate\Database\Eloquent\Model;

class Hint extends Model {

	protected $fillable = [ 'challenge_id', 'name', 'description', 'price' ];


	public function challenge()
	{
		return $this->belongsTo('Challenge');
	}

	public function users()
	{
		return $this->belongsToMany('User')
								->withTimestamps();
	}

}
