Summary:	A PyQt GUI for BitTorrent
Summary(pl):	Interfejs GUI do BitTorrenta
Name:		qtorrent
Version:	0.9.5
Release:	0.1
License:	MIT
Group:		Applications/Networking
Source0:	http://thegraveyard.org/files/%{name}-%{version}.tar.bz2
# Source0-md5:	5249c19a5d1bfec48bfb3f983a73818a
URL:		http://thegraveyard.org/qtorrent.php
BuildRequires:	python-PyQt	
Requires:	python-PyQt	
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QTorrent is a BitTorrent client that uses the Qt widget-set. It allows
you to have several torrents open at the same time from within the
same program window, offering you easy overview, access and management
through a list-mode. Every torrent also has it's own page where you
can control things like upload speed and upload slots. A page that
shows some statistics of all open torrents is also available.

%description -l pl
QTorrent jest klientem BitTorrenta u�ywaj�cym widget�w Qt. Pozwala na
otwarcie kilku torrent�w jednocze�nie w jednym oknie programu. Oferuje
�atwy podgl�d, dost�p i zarz�dzanie przez list�. Ka�dy torrent ma tak�e
w�asn� stron� przez kt�ra mo�na kontrolowa� szybko�� uploadu i sloty.
Strona te� przedstawia pewne statystyki wszystkich otwartych torrent�w.

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.txt MANIFEST PKG-INFO
%attr(755,root,root) %{_bindir}/*
%dir %{py_sitescriptdir}/pyqtorrent
%dir %{py_sitescriptdir}/pyqtorrent/BitTorrent
%{py_sitescriptdir}/pyqtorrent/*.py[co]
%{py_sitescriptdir}/pyqtorrent/BitTorrent/*.py[co]
