--TEST--
Bug #27742 (WDSL SOAP Parsing Schema bug)
--EXTENSIONS--
soap
--INI--
soap.wsdl_cache_enabled=0
--ENV--
LSAN_OPTIONS=detect_leaks=0
--FILE--
<?php
$x = new SoapClient(__DIR__."/bug27742.wsdl");
echo "ok\n";
?>
--EXPECT--
ok
