<?php

// if(trim($_POST['password'])!=trim($_POST['rpwd']))
// {
// 	exit('两次密码不一致,请返回上一页');
// }

$link = mysqli_connect('127.0.0.1:3306', 'Project_4', '123456') 
		or die ('连接失败 : ' . $mysqli->connect_error);
mysqli_select_db($link,'login_system');
mysqli_set_charset($link,'utf8');

$username=$_POST['username'];
$password=$_POST['password'];
 
$sql="insert into login_details values('$username','$password','$imgurl')";

$result=mysqli_query($link,$sql);
if($result){
	echo'Registration successful！';
}else{
	echo'Registration failed！';
}

mysqli_close($link);
?>
