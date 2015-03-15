<div class="content">

	<h2>Scoreboard</h2>
	<p>&nbsp;</p>

	<div class="col-md-2"></div>
	<div class="col-md-8">
		<div class="panel panel-default shadow">
			<div class="panel-body">
		<div id="scoreboard"></div>
		</div></div>
		<div class="panel panel-default shadow">
			<div class="panel-body">
				<table class="table">
					<thead>
						<tr>
						<th class="col-md-1">#</th>
							<th class="col-md-2">User</th>
							<th class="col-md-2">Course</th>
							<th class="col-md-2">Semester</th>
							<th class="col-md-2">Points</th>
						</tr>
					</thead>
					<tbody>
						<tr>
							<td>1</td>
							<td>c0d3z3r0</td>
							<td>UNITS</td>
							<td>4</td>
							<td>6000</td>
						</tr>
						<tr>
							<td>2</td>
							<td>c0d3z3r0</td>
							<td>UNITS</td>
							<td>4</td>
							<td>6000</td>
						</tr>
						<tr>
							<td>3</td>
							<td>c0d3z3r0</td>
							<td>UNITS</td>
							<td>4</td>
							<td>6000</td>
						</tr>
					</tbody>
				</table>
			</div>
		</div>
	</div>
	<div class="col-md-2"></div>

	<script type="text/javascript">
	var chart = c3.generate({
    bindto: '#scoreboard',
    data: {
      columns: [
        ['data1', 30, 200, 100, 400, 150, 250],
        ['data2', 50, 20, 10, 40, 15, 25]
      ]
    }
});
	</script>
</div>