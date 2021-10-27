<?php

function encodeResistorColors($ohmsString) {
    $col = "black brown red orange yellow green blue violet gray white gold";

    $i  = floatval($ohmsString) * (strpos($ohmsString, "k")?1000:(strpos($ohmsString, "M")?1000000:1));
    $c = explode(" ", $col);

    return (implode(" ", array($c[substr($i, 0, 1)], $c[substr($i, 1, 1)], $c[strlen(substr($i, 2))], $c[10] )));
}

encodeResistorColors("10 ohs");
encodeResistorColors("470 ohms");
encodeResistorColors("4.7k ohms");
encodeResistorColors("4.7M ohms");
encodeResistorColors("1M ohms");