# TODO:
# - add dir to store playlists and songs DB
# - add logrotate
Summary:	Music Player Daemon
Summary(hu.UTF-8):	Music Player Daemon
Summary(pl.UTF-8):	Music Player Daemon - demon odtwarzający muzykę
Name:		mpd
Version:	0.14_beta3
Release:	1
License:	GPL v2+
Group:		Applications/Multimedia
Source0:	http://downloads.sourceforge.net/musicpd/mpd-0.14_beta3.tar.bz2
# Source0-md5:	02320f13de6a84b53343f3f451c53ed1
Source1:	%{name}.conf
Source2:	%{name}.init
URL:		http://www.musicpd.org/
BuildRequires:	alsa-lib-devel >= 0.9.0
BuildRequires:	audiofile-devel >= 0.1.7
BuildRequires:	avahi-devel
BuildRequires:	faad2-devel >= 2.6.1
BuildRequires:	flac-devel >= 1.1.0
BuildRequires:	jack-audio-connection-kit-devel >= 0.4
BuildRequires:	libao-devel >= 0.8.3
BuildRequires:	libid3tag-devel
BuildRequires:	libmad-devel
BuildRequires:	libmikmod-devel >= 3.1.7
BuildRequires:	libmpcdec-devel
BuildRequires:	libogg-devel
BuildRequires:	libsamplerate-devel >= 0.0.15
BuildRequires:	libshout-devel
BuildRequires:	libvorbis-devel
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	pulseaudio-devel
BuildRequires:	zlib-devel
Provides:	group(mpd)
Provides:	user(mpd)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Music Player Daemon (MPD) allows remote access for playing music (MP3,
Ogg Vorbis, FLAC, AAC, Mod, and wave files) and managing playlists.
MPD is designed for integrating a computer into a stereo system that
provides control for music playback over a local network. It is also
makes a great desktop music player, especially if you are a console
junkie, like frontend options, or restart X often.

%description -l hu.UTF-8
Music Player Daemon (MPD)-vel lehetővé válik távoli zenelejátszás
(MP3, Ogg Vorbis, FLAC, AAC, Mod és wav fájlok) és lejátszási listák
menedzselése. Az MPD a számítógépben egy zenelejátszó, amelyet
irányíthatsz helyi hálózaton keresztül. Egyben egy zseniális desktop
zenelejátszó is, különösen a konzol-mániásoknak, vagy azoknak, akik
sűrűn indítják újra az X-et.

%description -l pl.UTF-8
Music Player Daemon (MPD) pozwala na zdalny dostęp do odtwarzania
muzyki (plików MP3, Ogg Vorbis, FLAC, AAC, Mod i wave) oraz
zarządzania playlistami. MPD jest zaprojektowany do integrowania
komputera w system stereo umożliwiający sterowanie odtwarzaniem muzyki
w sieci lokalnej. Służy także za dobry odtwarzacz muzyki dla
komputerów biurkowych, zwłaszcza dla miłośników konsoli, różnych opcji
frontendów albo często restartujących X.

%prep
%setup -q -n %{name}-0.14~beta3

%build
# ac_cv_* hacks to avoid unwanted linking
%configure \
	ac_cv_lib_iconv_main=no \
	ac_cv_lib_nsl_gethostbyname=no \
	--enable-ao
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_sysconfdir},/etc/rc.d/init.d}
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}
install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/mpd

%clean
rm -rf $RPM_BUILD_ROOT

%pre
%groupadd -g 204 mpd
%useradd -u 204 -r -d /home/services/mpd -s /bin/false -g audio -G mpd

%post
/sbin/chkconfig --add mpd

%preun
if [ "$1" = "0" ]; then
	%service mpd stop
	/sbin/chkconfig --del httpd
fi

%postun
if [ "$1" = "0" ]; then
	%userremove mpd
	%groupremove mpd
fi


%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO doc/mpdconf.example UPGRADING
%attr(755,root,root) %{_bindir}/*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/mpd.conf
%attr(754,root,root) /etc/rc.d/init.d/mpd
%{_mandir}/man1/mpd.1*
%{_mandir}/man5/mpd.conf.5*
