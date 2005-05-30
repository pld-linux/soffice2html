Summary:	StarOffice/OpenOffice.org document to HTML converter
Summary(pl):	Konwerter dokumentów StarOffice/OpenOffice.org do HTML-a
Name:		soffice2html
Version:	0.77
Release:	1
License:	unknown
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

%description -l pl
Konwertuje dokumenty StarOffice/OpenOffice.org na HTML-a, u¿ywaj±c
xsltproc do konwersji XML-a oraz converta z ImageMagicka do konwersji
obrazków. Tworzy równie¿ spis tre¶ci z odno¶nikami, obs³uguje tabele,
style, [spans] i wiele innych elementów XML-a z plików procesora.
U¿yteczny do konwersji dokumentów wsadowo, w³±czaj±c w to ¶rodowiska
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
