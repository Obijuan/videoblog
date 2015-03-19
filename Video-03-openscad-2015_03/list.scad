

l = [for (i=[0:4], a = 360 * i/5) [10 * sin(a), 10*cos (a)]];
echo(l);    
polygon(l);