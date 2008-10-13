# TODO: py_postclean
Summary:	A PyQt GUI for BitTorrent
Summary(pl.UTF-8):	Interfejs GUI do BitTorrenta
Name:		qtorrent
Version:	2.9.1
Release:	1
License:	MIT
Group:		Applications/Networking
Source0:	http://thegraveyard.org/files/%{name}-%{version}.tar.bz2
# Source0-md5:	3342c1df915941163d0b3f7f7aec0e83
URL:		http://thegraveyard.org/qtorrent.php
BuildRequires:	python >= 1:2.5
BuildRequires:	python-PyQt
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-libs
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

%description -l pl.UTF-8
QTorrent jest klientem BitTorrenta używającym widgetów Qt. Pozwala na
otwarcie kilku torrentów jednocześnie w jednym oknie programu. Oferuje
łatwy podgląd, dostęp i zarządzanie przez listę. Każdy potok
("torrent") ma także własną stronę przez która można kontrolować
szybkość uploadu i sloty. Strona też przedstawia pewne statystyki
wszystkich otwartych potoków.

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
%dir %{py_sitescriptdir}/pyqtorrent3
%dir %{py_sitescriptdir}/pyqtorrent3/BitTorrent
%dir %{py_sitescriptdir}/pyqtorrent3/QtGui
%{py_sitescriptdir}/pyqtorrent3/*.py[co]
%{py_sitescriptdir}/pyqtorrent3/*.py
%{py_sitescriptdir}/pyqtorrent3/BitTorrent/*.py[co]
%{py_sitescriptdir}/pyqtorrent3/BitTorrent/*.py
%{py_sitescriptdir}/pyqtorrent3/QtGui/*.py[co]
%{py_sitescriptdir}/pyqtorrent3/QtGui/*.py
%{py_sitescriptdir}/%{name}-%{version}-py*.egg-info
