<?php

function rgb($r,$g,$b){
    $r = min(max(0, $r), 255);
    $g = min(max(0, $g), 255);
    $b = min(max(0, $b), 255);

    return substr("000000".strtoupper(dechex($r*256*256 +($g *256) + $b)),-6);
}


rgb(255, 255, 255);