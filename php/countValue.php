<?php

static $count = 0;

function countValue()
{
    $GLOBALS["count"]++;
}

countValue();
countValue();
countValue();
var_dump($count);
