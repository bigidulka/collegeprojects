program z3_repeat;
var a,b,h,i,sum,ch:integer;
begin
  a:=3;b:=10;h:=6; ch:=a;
  repeat
    sum:=sum+ch; 
    ch:=ch+h; inc(i);
  until b<=i;
  writeln($'Среднее арифм: {sum/10} ', sum);
end.
