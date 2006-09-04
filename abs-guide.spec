Summary:	Advanced Bash Scripting Guide
Summary(pl):	Zaawansowany podrêcznik programowania w Bashu
Name:		abs-guide
Version:	4.0
Release:	3
License:	distributable
Group:		Documentation
Source0:	http://www.tldp.org/LDP/abs/%{name}.html.tar.gz
# Source0-md5:	7130fab7e9bd84a7b1bdfc655fe295b5
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

%description -l pl
Ten dokument jest podrêcznikiem programowania w Bashu, zawieraj±cym
tutorial i materia³y referencyjne. Do czytania nie wymaga wiedzy na
temat programowania czy pisania skryptów, ale szybko przechodzi do
instrukcji na ¶rednim i zaawansowanym poziomie. Æwiczenia i dobrze
skomentowane przyk³ady zachêcaj± do aktywnego uczestnictwa czytelnika.
Podrêcznik wci±¿ jest w trakcie pisania. Intencj± jest dodanie do
niego w przysz³ych wydaniach jak najwiêkszej ilo¶ci materia³ów
uzupe³niaj±cych, ¿eby wyewoluowa³ do wyczerpuj±cej ksi±¿ki
odpowiadaj±cej albo nawet przewy¿szaj±cej dostêpne podrêczniki
dotycz±ce pisania skryptów.

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
