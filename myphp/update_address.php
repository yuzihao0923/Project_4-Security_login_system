<?php

$link = mysqli_connect('127.0.0.1:3306', 'Project_4', '123456') 
		or die ('连接失败 : ' . $mysqli->connect_error);
mysqli_select_db($link,'login_system');
mysqli_set_charset($link,'utf8');


$username=$_POST['username'];
$password=$_POST['password'];
$imgurl=$_POST['img_url'];

$sql="update login_details set img_url = '$imgurl' where username = '$username' and password = '$password'";

$result=mysqli_query($link,$sql);
if($result){
    echo 'Update successful！';
    
    #Header("Location:http://192.168.246.201");
}else{
    echo 'Failed！';
}
mysqli_close($link);


?>