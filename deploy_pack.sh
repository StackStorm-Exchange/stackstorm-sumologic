#!/usr/bin/env bash

sudo st2 pack install git@github.com:copartit/st2-sumologic.git=master
sudo st2 pack register sumologic

