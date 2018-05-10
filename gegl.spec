#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gegl
Version  : 0.4.0
Release  : 23
URL      : https://download.gimp.org/pub/gegl/0.4/gegl-0.4.0.tar.bz2
Source0  : https://download.gimp.org/pub/gegl/0.4/gegl-0.4.0.tar.bz2
Summary  : Generic Graphics Library
Group    : Development/Tools
License  : BSD-3-Clause GPL-3.0 LGPL-3.0
Requires: gegl-bin
Requires: gegl-lib
Requires: gegl-data
Requires: gegl-locales
BuildRequires : docbook-xml
BuildRequires : gettext
BuildRequires : gobject-introspection-dev
BuildRequires : graphviz
BuildRequires : lcms2-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libxslt-bin
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(babl)
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(exiv2)
BuildRequires : pkgconfig(gdk-pixbuf-2.0)
BuildRequires : pkgconfig(gexiv2)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(json-glib-1.0)
BuildRequires : pkgconfig(lensfun)
BuildRequires : pkgconfig(libpng)
BuildRequires : pkgconfig(libraw)
BuildRequires : pkgconfig(librsvg-2.0)
BuildRequires : pkgconfig(libv4l2)
BuildRequires : pkgconfig(lua)
BuildRequires : pkgconfig(pango)
BuildRequires : pkgconfig(pangocairo)
BuildRequires : pkgconfig(pygobject-3.0)
BuildRequires : python
BuildRequires : ruby-dev

%description
GEGL-0.4.0
GEGL
GEGL
GEGL (Generic Graphics Library) is a data flow based image processing
framework, providing floating point processing and non-destructive
image processing capabilities to GNU Image Manipulation Program and
other projects (imgflo, GNOME Photos, gcut, iconographer, â¦)

%package bin
Summary: bin components for the gegl package.
Group: Binaries
Requires: gegl-data

%description bin
bin components for the gegl package.


%package data
Summary: data components for the gegl package.
Group: Data

%description data
data components for the gegl package.


%package dev
Summary: dev components for the gegl package.
Group: Development
Requires: gegl-lib
Requires: gegl-bin
Requires: gegl-data
Provides: gegl-devel

%description dev
dev components for the gegl package.


%package lib
Summary: lib components for the gegl package.
Group: Libraries
Requires: gegl-data

%description lib
lib components for the gegl package.


%package locales
Summary: locales components for the gegl package.
Group: Default

%description locales
locales components for the gegl package.


%prep
%setup -q -n gegl-0.4.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1524851195
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs "
%configure --disable-static --without-jasper --without-tiff --disable-docs PYTHON=/usr/bin/python3 --without-vala
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1524851195
rm -rf %{buildroot}
%make_install
%find_lang gegl-0.4

%files
%defattr(-,root,root,-)
/usr/lib64/gegl-0.4/grey2.json

%files bin
%defattr(-,root,root,-)
/usr/bin/gcut
/usr/bin/gegl
/usr/bin/gegl-imgcmp

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Gegl-0.4.typelib
/usr/share/gir-1.0/*.gir

%files dev
%defattr(-,root,root,-)
/usr/include/gegl-0.4/gegl-apply.h
/usr/include/gegl-0.4/gegl-audio-fragment.h
/usr/include/gegl-0.4/gegl-buffer-backend.h
/usr/include/gegl-0.4/gegl-buffer-cl-iterator.h
/usr/include/gegl-0.4/gegl-buffer-iterator.h
/usr/include/gegl-0.4/gegl-buffer.h
/usr/include/gegl-0.4/gegl-color.h
/usr/include/gegl-0.4/gegl-cpuaccel.h
/usr/include/gegl-0.4/gegl-curve.h
/usr/include/gegl-0.4/gegl-debug.h
/usr/include/gegl-0.4/gegl-enums.h
/usr/include/gegl-0.4/gegl-graph-debug.h
/usr/include/gegl-0.4/gegl-init.h
/usr/include/gegl-0.4/gegl-lookup.h
/usr/include/gegl-0.4/gegl-matrix.h
/usr/include/gegl-0.4/gegl-node.h
/usr/include/gegl-0.4/gegl-op.h
/usr/include/gegl-0.4/gegl-operations-util.h
/usr/include/gegl-0.4/gegl-paramspecs.h
/usr/include/gegl-0.4/gegl-path.h
/usr/include/gegl-0.4/gegl-plugin.h
/usr/include/gegl-0.4/gegl-processor.h
/usr/include/gegl-0.4/gegl-random.h
/usr/include/gegl-0.4/gegl-tile-backend.h
/usr/include/gegl-0.4/gegl-tile-handler.h
/usr/include/gegl-0.4/gegl-tile-source.h
/usr/include/gegl-0.4/gegl-tile.h
/usr/include/gegl-0.4/gegl-types.h
/usr/include/gegl-0.4/gegl-utils.h
/usr/include/gegl-0.4/gegl-version.h
/usr/include/gegl-0.4/gegl.h
/usr/include/gegl-0.4/npd/deformation.h
/usr/include/gegl-0.4/npd/graphics.h
/usr/include/gegl-0.4/npd/lattice_cut.h
/usr/include/gegl-0.4/npd/npd.h
/usr/include/gegl-0.4/npd/npd_common.h
/usr/include/gegl-0.4/npd/npd_debug.h
/usr/include/gegl-0.4/npd/npd_gegl.h
/usr/include/gegl-0.4/npd/npd_math.h
/usr/include/gegl-0.4/opencl/cl.h
/usr/include/gegl-0.4/opencl/cl_d3d10.h
/usr/include/gegl-0.4/opencl/cl_ext.h
/usr/include/gegl-0.4/opencl/cl_gl.h
/usr/include/gegl-0.4/opencl/cl_gl_ext.h
/usr/include/gegl-0.4/opencl/cl_platform.h
/usr/include/gegl-0.4/opencl/gegl-cl-color.h
/usr/include/gegl-0.4/opencl/gegl-cl-init.h
/usr/include/gegl-0.4/opencl/gegl-cl-random.h
/usr/include/gegl-0.4/opencl/gegl-cl-types.h
/usr/include/gegl-0.4/opencl/gegl-cl.h
/usr/include/gegl-0.4/opencl/opencl.h
/usr/include/gegl-0.4/operation/gegl-extension-handler.h
/usr/include/gegl-0.4/operation/gegl-operation-area-filter.h
/usr/include/gegl-0.4/operation/gegl-operation-composer.h
/usr/include/gegl-0.4/operation/gegl-operation-composer3.h
/usr/include/gegl-0.4/operation/gegl-operation-context.h
/usr/include/gegl-0.4/operation/gegl-operation-filter.h
/usr/include/gegl-0.4/operation/gegl-operation-handlers.h
/usr/include/gegl-0.4/operation/gegl-operation-meta-json.h
/usr/include/gegl-0.4/operation/gegl-operation-meta.h
/usr/include/gegl-0.4/operation/gegl-operation-point-composer.h
/usr/include/gegl-0.4/operation/gegl-operation-point-composer3.h
/usr/include/gegl-0.4/operation/gegl-operation-point-filter.h
/usr/include/gegl-0.4/operation/gegl-operation-point-render.h
/usr/include/gegl-0.4/operation/gegl-operation-property-keys.h
/usr/include/gegl-0.4/operation/gegl-operation-sink.h
/usr/include/gegl-0.4/operation/gegl-operation-source.h
/usr/include/gegl-0.4/operation/gegl-operation-temporal.h
/usr/include/gegl-0.4/operation/gegl-operation.h
/usr/include/gegl-0.4/sc/sc-common.h
/usr/include/gegl-0.4/sc/sc-context.h
/usr/include/gegl-0.4/sc/sc-outline.h
/usr/include/gegl-0.4/sc/sc-sample.h
/usr/lib64/pkgconfig/gegl-0.4.pc
/usr/lib64/pkgconfig/gegl-sc-0.4.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/gegl-0.4/gegl-common-gpl3.so
/usr/lib64/gegl-0.4/gegl-common.so
/usr/lib64/gegl-0.4/gegl-core.so
/usr/lib64/gegl-0.4/gegl-generated.so
/usr/lib64/gegl-0.4/jpg-load.so
/usr/lib64/gegl-0.4/jpg-save.so
/usr/lib64/gegl-0.4/lcms-from-profile.so
/usr/lib64/gegl-0.4/npd.so
/usr/lib64/gegl-0.4/npy-save.so
/usr/lib64/gegl-0.4/path.so
/usr/lib64/gegl-0.4/pixbuf.so
/usr/lib64/gegl-0.4/png-load.so
/usr/lib64/gegl-0.4/png-save.so
/usr/lib64/gegl-0.4/ppm-load.so
/usr/lib64/gegl-0.4/ppm-save.so
/usr/lib64/gegl-0.4/raw-load.so
/usr/lib64/gegl-0.4/rgbe-load.so
/usr/lib64/gegl-0.4/rgbe-save.so
/usr/lib64/gegl-0.4/save-pixbuf.so
/usr/lib64/gegl-0.4/seamless-clone-compose.so
/usr/lib64/gegl-0.4/seamless-clone.so
/usr/lib64/gegl-0.4/svg-load.so
/usr/lib64/gegl-0.4/text.so
/usr/lib64/gegl-0.4/transformops.so
/usr/lib64/gegl-0.4/v4l.so
/usr/lib64/gegl-0.4/vector-fill.so
/usr/lib64/gegl-0.4/vector-stroke.so
/usr/lib64/libgegl-0.4.so
/usr/lib64/libgegl-0.4.so.0
/usr/lib64/libgegl-0.4.so.0.400.0
/usr/lib64/libgegl-npd-0.4.so
/usr/lib64/libgegl-sc-0.4.so

%files locales -f gegl-0.4.lang
%defattr(-,root,root,-)

