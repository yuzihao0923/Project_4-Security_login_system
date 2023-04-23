<?php

$link = mysqli_connect('127.0.0.1:3306', 'Project_4', '123456') 
        or die ('连接失败 : ' . $link->connect_error);

mysqli_select_db($link,'login_system');
mysqli_set_charset($link,'utf8');

$username=$_POST['username'];
$password=$_POST['password'];
 
$sql="select * from login_details where username='$username' AND password='$password'";

$result=mysqli_query($link,$sql);
if($result->num_rows!=0){
    echo 'Login successful！';
    header("Location: face.html?username=$username");
    
    #Header("Location:http://192.168.246.201");
}else{
    echo 'Wrong account or password！';
}
mysqli_close($link);
?>