<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Data viz test</title>
</head>
<body>
    <h1>its aliveeeeee woop woop</h1>
    <p>testing 123 testing</p>
    <?php 
        echo 'php is running'; 
    ?>
    <?php
    try {
        $dbhost = 'localhost';
        $dbname='d3db';
        $dbuser = 'server';
        $dbpass = 'Espresso';

        $connection = new PDO("pgsql:host=$dbhost;dbname=$dbname", $dbuser, $dbpass);

        $sql = 'SELECT * FROM students';

        foreach ($connection->query($sql) as $row) {
            var_dump($row);
        }

        $connection = null;
    } catch (PDOException $e) {
        die("Error message: " . $e->getMessage());
    }
?>

</body>
</html>