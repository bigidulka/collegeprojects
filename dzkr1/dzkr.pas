var x: integer;
a,b,h,k: real;
begin
  writeln('Введите x: '); readln(x);
  
  if(x<-7) or ((log10(x)).ToString()='NaN') then writeln('Ур1, x не определен')
  else if (x<7) then writeln('Ур1, x<7: ',log10(x))
  else writeln('Ур1, любое другое кроме (x<-7 and x<7): ', log10(x));
  
  if((x>=-7) and (x<-1)) or ((6/power(x,0.1*x)-exp(x)/cos(2*x)).ToString()='NaN') then writeln('Ур2, x не определен')
  else if (x>1) and (x<=7) then writeln('Ур2, x>1 and x<=7: ', 6/power(x,0.1*x)-exp(x)/cos(2*x))
  else writeln('Ур2, x любое другое кроме (x>=-7 and x<-1 and x>1 and x<=7): ', 6/power(x,0.1*x)-exp(x)/cos(2*x));
  
  if(x>=-1) and (x<1) or (((sin(x)/power(x,2))*(log10(x)/ln(x))).ToString()='NaN') then writeln('Ур3, x не определен')
  else if (x>=1) then writeln('Ур3, x>=1: ', ((sin(x)/power(x,2))*(log10(x)/ln(x)))) 
  else if (x<>-1) then writeln('Ур3, x любое другое кроме (x>=-1 and x>=1): ', ((sin(x)/power(x,2))*(log10(x)/ln(x))));
  
  writeln('lg(x)-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------');
  a:=-9; b:=1; h:=0.1; k:=a;
  while k<=b do begin
    write(k:1:1, ' ~ ', log10(k), ' | ');
    k:=k+h;
  end;
  k:=a;
  writeln;
  writeln('6/power(x,0.1*x)-exp(x)/cos(2*x)---------------------------------------------------------------------------------------------------------------------------------------------------------');
   while k<=b do begin
    write(k:1:1, ' ~ ', 6/power(k,0.1*k)-exp(k)/cos(2*k), ' | ');
    k:=k+h;
  end;
  writeln;
  writeln('((sin(x)/power(x,2))*(log10(x)/ln(x)))---------------------------------------------------------------------------------------------------------------------------------------------------');
  k:=a;
   while k<=b do begin
    write(k:1:1, ' ~ ', ((sin(k)/power(k,2))*(log10(k)/ln(k))), ' | ');
    k:=k+h;
  end;
end.      