<?php
function checkRustdeskOnline($sourceId, $targetId, $serverIp, $serverPort = 21115) {
    // Build payload
    $sourceId = str_pad($sourceId, 10, "0", STR_PAD_LEFT);
    $payload = "\x68\xba\x01\x17\x0a\x0a" . $sourceId . "\x12\x09" . $targetId;

    // Opening TCP-Connection to RustDesk-Relay-Server
    $fp = stream_socket_client("tcp://{$serverIp}:{$serverPort}", $errno, $errstr, 5);

    if (!$fp) {
        echo "Verbindung fehlgeschlagen: $errstr ($errno)\n";
        return false;
    }

    // Sending Payload
    fwrite($fp, $payload);

    // Waiting for an answer (max 7 Byte)
    $response = fread($fp, 7);
    fclose($fp);

    // Check answers
    if ($response === "\x18\xc2\x01\x03\x0a\x01\x80") {
        return true; // Target is online
    } elseif ($response === "\x18\xc2\x01\x03\x0a\x01\x00") {
        return false; // Target is offline
    } else {
        echo "Unknown Answer: " . bin2hex($response) . "\n";
        return null;
    }
}


$serverIp = "1.1.1.1"; // Your Rustdesk Server IP
// Beispielnutzung:
$sourceId = "123456789";    // Mockup source ID to start communicating with your server
$targetId = "987654321";     // Target-ID

$isOnline = checkRustdeskOnline($sourceId, $targetId, $serverIp);
echo $isOnline === true ? "Target is online\n" :
     ($isOnline === false ? "Target is offline\n" : "State unknown\n");
?>
