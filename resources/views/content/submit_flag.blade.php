<div class="content content-middle">
	<h2>Submit a flag</h2>
	<p>&nbsp;</p>
	<form class="form-horizontal">
		<div class="form-group">
			<label class="col-md-4 control-label" for="flag"></label>
			<div class="input-group col-md-4">
				<input type="text" class="form-control" name="flag" placeholder="flag_78203e51ea0f3259087af0999dbce_" required>
				<span class="input-group-btn">
					<button id="submit" name="submit" class="btn btn-success">Submit</button>
				</span>
			</div>
		</div>

		<div id="msg_success" class="form-group">
			<label class="col-md-4 control-label"></label>
			<div class="alert alert-success col-md-4 shadow">
				<span class="glyphicon glyphicon-ok"></span> Success!
			</div>
		</div>
		<div id="msg_info" class="form-group hidden">
			<label class="col-md-4 control-label"></label>
			<div class="alert alert-info col-md-4 shadow">
				<span class="glyphicon glyphicon-repeat"></span> Flag already submitted.
			</div>
		</div>
		<div id="msg_error" class="form-group hidden">
			<label class="col-md-4 control-label"></label>
			<div class="alert alert-danger col-md-4 shadow">
				<span class="glyphicon glyphicon-remove"></span> Wrong flag submitted!
			</div>
		</div>
	</form>
</div>