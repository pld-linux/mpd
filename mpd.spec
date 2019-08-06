# TODO:
# - add logrotate
#
# Conditional build:
%bcond_without	mod		# MOD support via libmikmod
%bcond_without	pulseaudio	# PulseAudio support
%bcond_without	audiofile	# Audiofile support (WAV and others)

Summary:	Music Player Daemon
Summary(pl.UTF-8):	Music Player Daemon - demon odtwarzający muzykę
Name:		mpd
Version:	0.21.13
Release:	1
License:	GPL v2+
Group:		Applications/Multimedia
Source0:	http://www.musicpd.org/download/mpd/0.21/%{name}-%{version}.tar.xz
# Source0-md5:	75cbeb271e2a8a3ec8cd08eee2e97fb3
Source1:	%{name}.conf
Source2:	%{name}.init
Source3:	%{name}.sysconfig
Source4:	%{name}.tmpfiles
URL:		http://www.musicpd.org/
BuildRequires:	OpenAL-devel
BuildRequires:	adplug-devel
BuildRequires:	alsa-lib-devel >= 0.9.0
%{?with_audiofile:BuildRequires:	audiofile-devel >= 0.3}
BuildRequires:	avahi-devel
BuildRequires:	boost-devel >= 1.58
BuildRequires:	bzip2-devel
BuildRequires:	curl-devel >= 7.18
BuildRequires:	dbus-devel
BuildRequires:	doxygen
BuildRequires:	expat-devel
BuildRequires:	faad2-devel >= 2.6.1-5
BuildRequires:	ffmpeg-devel >= 2.4.0
BuildRequires:	flac-devel >= 1.2.0
BuildRequires:	fluidsynth-devel >= 1.1
BuildRequires:	game-music-emu-devel
BuildRequires:	gcc >= 6:5
BuildRequires:	glib2-devel >= 1:2.28.0
BuildRequires:	jack-audio-connection-kit-devel >= 0.100
BuildRequires:	lame-libs-devel
BuildRequires:	libao-devel >= 0.8.3
BuildRequires:	libcdio-devel
BuildRequires:	libcdio-paranoia-devel >= 0.4
BuildRequires:	libcue-devel
BuildRequires:	libicu-devel >= 50
BuildRequires:	libid3tag-devel
BuildRequires:	libmad-devel
%{?with_mod:BuildRequires:	libmikmod-devel >= 3.2}
BuildRequires:	libmms-devel >= 0.4
BuildRequires:	libmodplug-devel
BuildRequires:	libmpdclient-devel >= 2.9
BuildRequires:	libmpg123-devel
BuildRequires:	libnfs-devel >= 1.11
BuildRequires:	libogg-devel
BuildRequires:	libsamplerate-devel >= 0.1.3
BuildRequires:	libshout-devel
BuildRequires:	libsidplay2-devel >= 2.1.1-5
BuildRequires:	libsmbclient-devel >= 0.2
BuildRequires:	libsndfile-devel
BuildRequires:	libstdc++-devel >= 0.2
BuildRequires:	libupnp-devel
BuildRequires:	libvorbis-devel
BuildRequires:	libwrap-devel
BuildRequires:	meson >= 0.49.0
BuildRequires:	musepack-devel
BuildRequires:	ninja
BuildRequires:	opus-devel
BuildRequires:	pkgconfig >= 1:0.9.0
%{?with_pulseaudio:BuildRequires:	pulseaudio-devel >= 0.9.16}
BuildRequires:	rpmbuild(macros) >= 1.727
BuildRequires:	shine-devel >= 3.1
BuildRequires:	soxr-devel
BuildRequires:	sphinx-pdg
BuildRequires:	sqlite3-devel >= 3.7.3
BuildRequires:	systemd-devel
BuildRequires:	twolame-devel
BuildRequires:	wavpack-devel
BuildRequires:	wildmidi-devel
BuildRequires:	xmlto
BuildRequires:	yajl-devel >= 2.0
BuildRequires:	zlib-devel
BuildRequires:	zziplib-devel >= 0.13
Requires(post,postun):	gtk-update-icon-cache
Requires(post,preun,postun):	systemd-units >= 38
Requires:	alsa-lib >= 0.9.0
%{?with_audiofile:Requires:	audiofile >= 0.3}
Requires:	curl-libs >= 7.18
Requires:	faad2-libs >= 2.6.1-5
Requires:	ffmpeg-libs >= 2.4.0
Requires:	flac >= 1.2.0
Requires:	fluidsynth >= 1.1
Requires:	glib2 >= 1:2.28.0
Requires:	hicolor-icon-theme
Requires:	jack-audio-connection-kit-libs >= 0.100
Requires:	libao >= 0.8.3
Requires:	libcdio-paranoia >= 0.4
Requires:	libicu >= 50
%{?with_mod:Requires:	libmikmod >= 3.2}
Requires:	libmms >= 0.4
Requires:	libmpdclient >= 2.9
Requires:	libnfs >= 1.11
Requires:	libsamplerate >= 0.1.3
Requires:	libsidplay2 >= 2.1.1-5
Requires:	libsmbclient >= 0.2
%{?with_pulseaudio:Requires:	pulseaudio-libs >= 0.9.16}
Requires:	shine >= 3.1
Requires:	sqlite3 >= 3.7.3
Requires:	systemd-units >= 38
Requires:	yajl >= 2.0
Requires:	zziplib >= 0.13
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

%package doc
Summary:	Documentation for Music Player Daemon (MPD)
Summary(fr.UTF-8):	Documentation pour Music Player Daemon (MPD)
Summary(it.UTF-8):	Documentazione di Music Player Daemon (MPD)
Summary(pl.UTF-8):	Podręcznik dla Music Player Daemon (MPD)
Group:		Documentation
Obsoletes:	mpd-apidocs < 0.21

%description doc
Documentation for Music Player Daemon (MPD).

%description doc -l fr.UTF-8
Documentation pour Music Player Daemon (MPD).

%description doc -l it.UTF-8
Documentazione di Music Player Daemon (MPD).

%description doc -l pl.UTF-8
Dokumentacja do Music Player Daemon (MPD).

%prep
%setup -q

%build
%meson build \
	-Dpulse=%{?with_pulseaudio:enabled}%{!?with_pulseaudio:disabled} \
	-Dmikmod=%{?with_mod:enabled}%{!?with_mod:disabled} \
	-Dadplug=enabled \
	-Dalsa=enabled \
	-Dao=enabled \
	-Daudiofile=%{?with_audiofile:enabled}%{!?with_audiofile:disabled} \
	-Dbzip2=enabled \
	-Dcdio-paranoia=enabled \
	-Dcurl=enabled \
	-Ddatabase=true \
	-Ddocumentation=true \
	-Ddsd=true \
	-Dexpat=enabled \
	-Dffmpeg=enabled \
	-Dfifo=true \
	-Dflac=enabled \
	-Dfluidsynth=enabled \
	-Dgme=enabled \
	-Dhttpd=true \
	-Dicu=enabled \
	-Did3=enabled \
	-Dinotify=true \
	-Dipv6=enabled \
	-Diso9660=enabled \
	-Djack=enabled \
	-Dlame-encoder=enabled \
	-Dlibmpdclient=enabled \
	-Dlibwrap=enabled \
	-Dlsr=enabled \
	-Dmad=enabled \
	-Dmikmod=enabled \
	-Dmms=enabled \
	-Dmodplug=enabled \
	-Dmpcdec=disabled \
	-Dnfs=enabled \
	-Dopenal=enabled \
	-Dopus=enabled \
	-Doss=enabled \
	-Dpipe=true \
	-Drecorder=true \
	-Dsidplay=enabled \
	-Dshine-encoder=enabled \
	-Dshout=enabled \
	-Dsmbclient=enabled \
	-Dsndfile=enabled \
	-Dsoundcloud=enabled \
	-Dsoxr=enabled \
	-Dsqlite=enabled \
	-Ddaemon=true \
	-Dsystemd=enabled \
	-Dtcp=true \
	-Dtwolame-encoder=enabled \
	-Dupnp=enabled \
	-Dun=enabled \
	-Dvorbis=enabled \
	-Dvorbis-encoder=enabled \
	-Dwave_encoder=true \
	-Dwavpack=enabled \
	-Dwildmidi=enabled \
	-Dzlib=enabled \
	-Dzzip=enabled \
	-Dzeroconf=avahi \
	-Dsystemd_system_unit_dir=%{systemdunitdir} \
	-Dsystemd_user_unit_dir=%{systemduserunitdir}
%meson_build -C build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},/etc/{rc.d/init.d,sysconfig}} \
	$RPM_BUILD_ROOT{/var/lib/mpd/playlists,/var/log/mpd,/var/run/mpd} \
	$RPM_BUILD_ROOT%{systemdtmpfilesdir}

%meson_install -C build

cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}
install -p %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/mpd
cp -p %{SOURCE3} $RPM_BUILD_ROOT/etc/sysconfig/mpd
cp -p %{SOURCE4} $RPM_BUILD_ROOT%{systemdtmpfilesdir}/%{name}.conf

touch $RPM_BUILD_ROOT/var/lib/mpd/mpd.db
touch $RPM_BUILD_ROOT/var/lib/mpd/mpdstate
touch $RPM_BUILD_ROOT/var/lib/mpd/sticker.sql
touch $RPM_BUILD_ROOT/var/log/mpd/mpd.log

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/mpd

%clean
rm -rf $RPM_BUILD_ROOT

%pre
%groupadd -g 204 mpd
%useradd -u 204 -r -d /var/lib/mpd -s /bin/false -c "Music Player Daemon (MPD) user" -G audio -g mpd mpd

%post
for f in mpd.log; do
	if [ ! -f /var/log/%{name}/$f ]; then
		touch /var/log/%{name}/$f
		chown mpd:mpd /var/log/%{name}/$f
		chmod 644 /var/log/%{name}/$f
	fi
done
/sbin/chkconfig --add mpd
%systemd_post %{name}.service %{name}.socket
%update_icon_cache hicolor

%preun
if [ "$1" = "0" ]; then
	%service mpd stop
	/sbin/chkconfig --del mpd
fi
%systemd_preun %{name}.service %{name}.socket

%postun
if [ "$1" = "0" ]; then
	%userremove mpd
	%groupremove mpd
fi
%systemd_reload
%update_icon_cache hicolor

%triggerpostun -- %{name} < 0.16.6-1
%systemd_trigger %{name}.service

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md doc/mpdconf.example
%attr(755,root,root) %{_bindir}/*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/mpd.conf
%attr(754,root,root) /etc/rc.d/init.d/mpd
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/mpd
%{systemdtmpfilesdir}/%{name}.conf
%{systemdunitdir}/mpd.service
%{systemdunitdir}/mpd.socket
%{systemduserunitdir}/mpd.service
%{systemduserunitdir}/mpd.socket
%dir %attr(770,root,mpd) /var/lib/%{name}
%dir %attr(770,root,mpd) /var/lib/%{name}/playlists
%dir %attr(751,root,root) /var/log/%{name}
%dir %attr(770,root,mpd) /var/run/%{name}
%attr(644,mpd,mpd) %ghost /var/lib/%{name}/mpd.db
%attr(644,mpd,mpd) %ghost /var/lib/%{name}/mpdstate
%attr(644,mpd,mpd) %ghost /var/lib/%{name}/sticker.sql
%attr(644,mpd,mpd) %ghost /var/log/%{name}/mpd.log
%{_iconsdir}/hicolor/scalable/apps/mpd.svg
%{_mandir}/man1/mpd.1*
%{_mandir}/man5/mpd.conf.5*

%files doc
%defattr(644,root,root,755)
%doc build/doc/html
