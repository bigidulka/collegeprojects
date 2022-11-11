program z4_repeat;
var n,i,sum,k:integer;
begin
  write('Введите количество вводимых чисел: '); read(n);
  repeat
    write($'Введите число {i}: '); readln(k); sum:=sum+k; inc(i);
  until i>=n;
  writeln($'Сумма {sum}, Ср.Ар {sum/n}');
end.
