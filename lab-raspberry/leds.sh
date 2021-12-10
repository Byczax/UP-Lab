#!/bin/bash

gpio -1 mode 40 out # ustawienie pinu jako wyjscie
gpio -1 write 40 1 # wlaczenie diody
gpio -1 write 40 0 # wylaczenie diody
gpio -1 blink 40 # wlaczenie trybu migania diody