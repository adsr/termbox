Summary:         A legacy-free alternative to ncurses
Name:            termbox
Version:         1.1.2
Release:         1%{?dist}
License:         MIT
URL:             https://github.com/nsf/termbox
Source:          https://github.com/nsf/termbox/archive/v%{version}.tar.gz

BuildRequires:   python

%description
Termbox is a library that provides minimalistic API which allows the 
programmer to write text-based user interfaces.

It is based on a very simple abstraction. The main idea is viewing 
terminals as a table of fixed-size cells and input being a stream of 
structured messages. Would be fair to say that the model is inspired 
by windows console API. The abstraction itself is not perfect and it 
may create problems in certain areas. The most sensitive ones are 
copy & pasting and wide characters (mostly Chinese, Japanese, Korean 
(CJK) characters). When it comes to copy & pasting, the notion of 
cells is not really compatible with the idea of text. And CJK runes 
often require more than one cell to display them nicely. Despite the 
mentioned flaws, using such a simple model brings benefits in a form 
of simplicity. And KISS principle is important.

At this point one should realize, that CLI (command-line interfaces) 
aren't really a thing termbox is aimed at. But rather 
pseudo-graphical user interfaces.

%package devel
Summary: Development files for the termbox library

%description devel
The header files and libraries for developing applications that use 
the termbox library. Install the termbox-devel package if you want to
develop applications which will use termbox.

%package static
Summary: Static libraries for termbox

%description static
The termbox-static package includes static libraries for termbox.

%prep
%setup -q

%build
./waf configure \
    --prefix=%{_prefix} \
    --libdir=%{_libdir} \
    --includedir=%{_includedir}
./waf %{?_smp_mflags} -v

%install
./waf --destdir=$RPM_BUILD_ROOT -v install

%files
%{_libdir}/libtermbox.so
%{_libdir}/libtermbox.so.1
%{_libdir}/libtermbox.so.1.*

%files devel
%{_includedir}/termbox.h

%files static
%{_libdir}/libtermbox.a

%changelog
* Fri Sep 13 2019 Adam Saponara <as@php.net> - 1.1.2-1
- initial spec
