--TEST--
Test CURLMOPT_PUSHFUNCTION with non-existent callback function
--CREDITS--
Davey Shafik
Kévin Dunglas
Niels Dossche
--EXTENSIONS--
curl
--XLEAK--
--SKIPIF--
<?php
include 'skipif-nocaddy.inc';

$curl_version = curl_version();
if ($curl_version['version_number'] < 0x080100) {
    exit("skip: test may crash with curl < 8.1.0");
}
?>
--FILE--
<?php
// Test adapted from curl_pushfunction.phpt

$mh = curl_multi_init();

curl_multi_setopt($mh, CURLMOPT_PIPELINING, CURLPIPE_MULTIPLEX);
curl_multi_setopt($mh, CURLMOPT_PUSHFUNCTION, "nonexistent");

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, "https://localhost/serverpush");
curl_setopt($ch, CURLOPT_HTTP_VERSION, CURL_HTTP_VERSION_2_0);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);

curl_multi_add_handle($mh, $ch);

$active = null;
while(true) {
    $status = curl_multi_exec($mh, $active);

    do {
        $info = curl_multi_info_read($mh);
        if (false !== $info && $info['msg'] == CURLMSG_DONE) {
            $handle = $info['handle'];
            if ($handle !== null) {
                curl_multi_remove_handle($mh, $handle);
                curl_close($handle);
                break 2;
            }
        }
    } while ($info);
}

curl_multi_close($mh);
?>
--EXPECTF--
Warning: curl_multi_exec(): Cannot call the CURLMOPT_PUSHFUNCTION in %s on line %d
