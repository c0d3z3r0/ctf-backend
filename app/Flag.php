<?php namespace App;

use Illuminate\Database\Eloquent\Model;

class Flag extends Model {

	protected $fillable = [ 'challenge_id', 'flag', 'credits' ];

	protected $hidden = [ 'flag' ];

	public function challenge()
	{
		return $this->belongsTo('Challenge');
	}

	public function users()
	{
		return $this->belongsToMany('User')
								->withTimestamps()
								->withPivot('solution');
	}

}
