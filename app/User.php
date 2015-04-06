<?php namespace App;

use Illuminate\Auth\Authenticatable;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Auth\Passwords\CanResetPassword;
use Illuminate\Contracts\Auth\Authenticatable as AuthenticatableContract;
use Illuminate\Contracts\Auth\CanResetPassword as CanResetPasswordContract;

class User extends Model implements AuthenticatableContract, CanResetPasswordContract {

	use Authenticatable, CanResetPassword;

	protected $fillable = [ 'name', 'email', 'password', 'confirmed' ,'confirmation_code' ];

	protected $hidden = [ 'password', 'confirmation_code', 'remember_token' ];


	public function flags()
	{
		return $this->belongsToMany('User')
								->withTimestamps()
								->withPivot('solution');
	}

	public function hints()
	{
		return $this->belongsToMany('Hint')
								->withTimestamps();
	}

}
