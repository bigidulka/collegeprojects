program bl_4_z5; //25
var a,b,c,d,e,f, kopt, kopd: integer;
begin
  print('Введите стоимость товара(рубли и копейки): '); readln(a, b);
  print('Введите плату(рубли копейки): '); readln(c, d);
  kopd:=a*100+b;
  kopt:=c*100+d;
  if (kopt-kopd)>0 then begin f:=(kopt-kopd) div 100; e:=(kopt-kopd) mod 100; print('Сдача: ', f, ' Рублей ', e, ' Копеек'); end
  else if (kopt-kopd)<0 then print('не хватает денег');
  if (kopt-kopd)=0 then print('cсдачи не будет');
end.