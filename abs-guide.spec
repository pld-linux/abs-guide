Summary:	Advanced Bash Scripting Guide
Summary(pl.UTF-8):   Zaawansowany podręcznik programowania w Bashu
Name:		abs-guide
Version:	4.2.01
Release:	1
License:	distributable
Group:		Documentation
Source0:	http://www.tldp.org/LDP/abs/%{name}.html.tar.gz
# Source0-md5:	b12da00899cb2c1d3ca3e96605f9c6c3
URL:		http://www.tldp.org/LDP/abs/html/index.html
Requires:	LDP-base
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This document is both a tutorial and a reference on shell scripting
with Bash. It assumes no previous knowledge of scripting or
programming, but progresses rapidly toward an intermediate/advanced
level of instruction. The exercises and heavily-commented examples
invite active reader participation. Still, it is a work in progress.
The intention is to add much supplementary material in future updates
to this document, as it evolves into a comprehensive book that matches
or surpasses any of the shell scripting manuals in print.

%description -l pl.UTF-8
Ten dokument jest podręcznikiem programowania w Bashu, zawierającym
tutorial i materiały referencyjne. Do czytania nie wymaga wiedzy na
temat programowania czy pisania skryptów, ale szybko przechodzi do
instrukcji na średnim i zaawansowanym poziomie. Ćwiczenia i dobrze
skomentowane przykłady zachęcają do aktywnego uczestnictwa czytelnika.
Podręcznik wciąż jest w trakcie pisania. Intencją jest dodanie do
niego w przyszłych wydaniach jak największej ilości materiałów
uzupełniających, żeby wyewoluował do wyczerpującej książki
odpowiadającej albo nawet przewyższającej dostępne podręczniki
dotyczące pisania skryptów.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_docdir}/LDP/abs-guide
cp -a * $RPM_BUILD_ROOT%{_docdir}/LDP/abs-guide

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_docdir}/LDP/abs-guide
