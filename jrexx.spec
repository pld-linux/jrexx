Summary:	Automaton based regular expression API for Java
Summary(pl.UTF-8):	API wyrażeń regularnych dla Javy oparte na automatach
Name:		jrexx
Version:	1.1.1
Release:	0.1
License:	LGPL
Group:		Development/Languages/Java
Source0:	http://dl.sourceforge.net/jrexx/%{name}-%{version}-src.zip
# Source0-md5:	e54e1dc8454472ef2706bc21768df103
Source1:	%{name}-build.xml
URL:		http://www.karneim.com/jrexx/
BuildRequires:	ant >= 0:1.5.4
BuildRequires:	jpackage-utils >= 0:1.5.32
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	unzip
%if %(locale -a | grep -q '^en_US$'; echo $?)
BuildRequires:	glibc-localedb-all
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
jrexx is a powerful easy-to-use regular expression API for textual
pattern matching. Technically jrexx uses a minimized deterministic FSA
(finite state automaton) and compiles the textual representation of
the regular expression into such an automaton. Besides the usual
pattern matching functionality, jrexx provides an introspection API
for exploration of the automaton's structure by 'states' and
'transitions'. Since the automaton is deterministic and minimized the
pattern matching alogorithm is extremly fast (compared to the Java
regular expression API in JDK 1.4) and works with huge patterns and
input texts. Since FSA can be handled as sets, jrexx also offers all
basic set operations for complement, union, intersection and
difference, which is not provided by other regex implementations (as
far as we know).

%description -l pl.UTF-8
jrexx to mające duże możliwości, łatwe w użyciu API wyrażeń
regularnych do dopasowywania wzorców tekstowych. Od strony technicznej
jrexx używa minimalnej wersji deterministycznych FSA (automatów
skończonych) i kompiluje tekstowe reprezentacje wyrażeń regularnych do
takich automatów. Poza zwykłą funkcją dopasowywania wzorców jrexx
udostępnia API introspekcyjne do przeglądania struktury automatu przez
stany (statet) i przejścia (transitions). Ponieważ automat jest
deterministyczny i zminimalizowany, algorytm dopasowywania jest bardzo
szybki (w porównaniu do API wyrażeń regularnych Javy w JDK 1.4) i
działa z dużymi wzorcami oraz tekstami wejściowymi. Ponieważ FSA są
obsługiwane jako zbiory, jrexx oferuje także wszystkie podstawowe
operacje na zbiorach (dopełnienie, sumę, przecięcie i różnicę), nie
dostępne w innych implementacjach wyrażeń regularnych (wg wiedzy
autorów).

%package javadoc
Summary:	Javadoc for %{name}
Summary(pl.UTF-8):	Dokumentacja Javadoc do pakietu jrexx
Group:		Documentation
Requires:	jpackage-utils

%description javadoc
Javadoc documentation for %{name}.

%description javadoc -l pl.UTF-8
Dokumentacja Javadoc do pakietu jrexx.

%prep
%setup -q -T -c %{name}-%{version}
unzip -q %{SOURCE0}
cp %{SOURCE1} build.xml

%build
export LC_ALL=en_US # source code not US-ASCII
%ant dist

%install
rm -rf $RPM_BUILD_ROOT

# jars
install -d $RPM_BUILD_ROOT%{_javadir}
cp -a output/dist/lib/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# javadoc
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -a output/dist/jdoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -nfs %{name}-%{version} %{_javadocdir}/%{name}

%files
%defattr(644,root,root,755)
%{_javadir}/*.jar

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}
