program z2_repeat;
var a,b, sum, pr:longint;
begin
  sum:=0; pr:=1;
  write('Введите диапазон четных натуральных(a<b): '); read(a,b);
  repeat 
    if(a mod 2<>0)then sum:=sum+a
    else pr:=pr*a; inc(a);
  until a>b;
  writeln($'Сумма нечетных {sum}, Произведение четных {pr}');
end.
