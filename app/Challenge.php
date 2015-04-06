<?php namespace App;

use Illuminate\Database\Eloquent\Model;

class Challenge extends Model {

	protected $fillable = [ 'name', 'description', 'link' ];


	public function categories()
	{
		return $this->belongsToMany('Category')
								->withTimestamps();
	}

	public function flags()
	{
		return $this->hasMany('Flag');
	}

	public function hints()
	{
		return $this->hasMany('Hint');
	}

}
