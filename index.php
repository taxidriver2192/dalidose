<?php

$api_key = 'H6kiaHNQrzP8YVhjILHDYvgQowhxfMbzVjUP3zUs';
$headers = [
    'Authorization: Basic ' . base64_encode($api_key),
    'Content-Type: application/json'
];

$url = 'https://api.printful.com/store/products';

$options = [
    'http' => [
        'header' => implode("\r\n", $headers),
        'method' => 'GET'
    ]
];

$context = stream_context_create($options);
$response = file_get_contents($url, false, $context);
$response_data = json_decode($response, true);

$response_code = explode(' ', $http_response_header[0])[1];

if ($response_code == 200) {
    echo "API key is working, products retrieved successfully";
} else {
    echo "Error (Code: " . $response_code . "): " . $response_data["error"]["message"] . "<br>";
    echo "Detailed Error: <pre>" . json_encode($response_data["error"], JSON_PRETTY_PRINT) . "</pre>";
}
