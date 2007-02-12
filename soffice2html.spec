Summary:	StarOffice/OpenOffice.org document to HTML converter
Summary(pl.UTF-8):   Konwerter dokumentów StarOffice/OpenOffice.org do HTML-a
Name:		soffice2html
Version:	0.77
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	http://hoopajoo.net/static/projects/%{name}-%{version}.tar.gz
# Source0-md5:	dd5d3ed417db4c1fd9cc77c9ae4122aa
URL:		http://hoopajoo.net/projects/soffice2html.html
Requires:	ImageMagick
Requires:	libxslt-progs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Converts a StarOffice/OpenOffice.org document to HTML, using xsltproc
for the XML conversion and ImageMagick's convert to convert images.
Also create a table of contents with links, handles tables, styles,
spans, and many other XML elements from a writer file. Useful to
convert documents in a batch manner, including in a web or CGI
environment.

%description -l pl.UTF-8
Konwertuje dokumenty StarOffice/OpenOffice.org na HTML-a, używając
xsltproc do konwersji XML-a oraz converta z ImageMagicka do konwersji
obrazków. Tworzy również spis treści z odnośnikami, obsługuje tabele,
style, [spans] i wiele innych elementów XML-a z plików procesora.
Użyteczny do konwersji dokumentów wsadowo, włączając w to środowiska
WWW oraz CGI.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install soffice2html.pl $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/*
