module ngon(num, r) {
  polygon([for (i=[0:num-1], a=i*360/num) [ r*cos(a), r*sin(a) ]]);
}

*ngon(3, 10);
*translate([20,0]) ngon(6, 8);
*translate([36,0]) ngon(10, 6);


l = [for (i=[0:5]) [10 * sin(360 * i / 5), 10*cos (360 * i / 5)]];
    polygon(l);
echo(l);    
