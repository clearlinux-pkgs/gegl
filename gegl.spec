#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gegl
Version  : 0.4.20
Release  : 54
URL      : https://download.gimp.org/pub/gegl/0.4/gegl-0.4.20.tar.xz
Source0  : https://download.gimp.org/pub/gegl/0.4/gegl-0.4.20.tar.xz
Summary  : Provides gif loading and conversion
Group    : Development/Tools
License  : BSD-3-Clause GPL-3.0 LGPL-3.0 MIT
Requires: gegl-bin = %{version}-%{release}
Requires: gegl-data = %{version}-%{release}
Requires: gegl-lib = %{version}-%{release}
Requires: gegl-license = %{version}-%{release}
Requires: gegl-locales = %{version}-%{release}
BuildRequires : SDL2-dev
BuildRequires : buildreq-meson
BuildRequires : gexiv2-dev
BuildRequires : gobject-introspection-dev
BuildRequires : graphviz
BuildRequires : lcms2-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : librsvg
BuildRequires : librsvg-dev
BuildRequires : libwebp-dev
BuildRequires : openexr-dev
BuildRequires : perl
BuildRequires : pkgconfig(babl)
BuildRequires : pkgconfig(gdk-pixbuf-2.0)
BuildRequires : pkgconfig(json-glib-1.0)
BuildRequires : pkgconfig(lensfun)
BuildRequires : pkgconfig(libavutil)
BuildRequires : pkgconfig(libraw)
BuildRequires : pkgconfig(librsvg-2.0)
BuildRequires : pkgconfig(libspiro)
BuildRequires : pkgconfig(libswscale)
BuildRequires : pkgconfig(libv4l1)
BuildRequires : pkgconfig(libv4l2)
BuildRequires : pkgconfig(luajit)
BuildRequires : pkgconfig(pango)
BuildRequires : pkgconfig(pangocairo)
BuildRequires : pkgconfig(poppler-glib)
BuildRequires : pkgconfig(pygobject-3.0)
BuildRequires : python3
BuildRequires : ruby-dev
BuildRequires : vala

%description
========================================================================
====  Poly2Tri-C: A library for generating, refining and rendering  ====
====        2-Dimensional Constrained Delaunay Triangulations       ====
========================================================================

%package bin
Summary: bin components for the gegl package.
Group: Binaries
Requires: gegl-data = %{version}-%{release}
Requires: gegl-license = %{version}-%{release}

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
Requires: gegl-lib = %{version}-%{release}
Requires: gegl-bin = %{version}-%{release}
Requires: gegl-data = %{version}-%{release}
Provides: gegl-devel = %{version}-%{release}
Requires: gegl = %{version}-%{release}

%description dev
dev components for the gegl package.


%package lib
Summary: lib components for the gegl package.
Group: Libraries
Requires: gegl-data = %{version}-%{release}
Requires: gegl-license = %{version}-%{release}

%description lib
lib components for the gegl package.


%package license
Summary: license components for the gegl package.
Group: Default

%description license
license components for the gegl package.


%package locales
Summary: locales components for the gegl package.
Group: Default

%description locales
locales components for the gegl package.


%prep
%setup -q -n gegl-0.4.20
cd %{_builddir}/gegl-0.4.20

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1579636104
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/gegl
cp %{_builddir}/gegl-0.4.20/COPYING %{buildroot}/usr/share/package-licenses/gegl/7181028b2cb15912d89c76ca33b720a3bfb537cc
cp %{_builddir}/gegl-0.4.20/COPYING.LESSER %{buildroot}/usr/share/package-licenses/gegl/e7d563f52bf5295e6dba1d67ac23e9f6a160fab9
cp %{_builddir}/gegl-0.4.20/subprojects/libnsgif/COPYING %{buildroot}/usr/share/package-licenses/gegl/91664a5e5a2b5bf020a621d0e9c5cc507e619c94
cp %{_builddir}/gegl-0.4.20/subprojects/poly2tri-c/COPYING %{buildroot}/usr/share/package-licenses/gegl/7cd64aeec55f96676d9e34b6b1677ec470e45fcf
cp %{_builddir}/gegl-0.4.20/subprojects/poly2tri-c/LICENSE-Poly2Tri-C.txt %{buildroot}/usr/share/package-licenses/gegl/855d3492027e24b96cc759b7fa729176cb1bdca7
cp %{_builddir}/gegl-0.4.20/subprojects/poly2tri-c/LICENSE-Poly2Tri.txt %{buildroot}/usr/share/package-licenses/gegl/178f030d76bde249653291b58a7e8066755051be
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang gegl-0.4

%files
%defattr(-,root,root,-)
/usr/lib64/gegl-0.4/grey2.json

%files bin
%defattr(-,root,root,-)
/usr/bin/gegl
/usr/bin/gegl-imgcmp

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Gegl-0.4.typelib
/usr/share/gegl-0.4/lua/cairo.lua
/usr/share/gegl-0.4/lua/cairo_h.lua
/usr/share/gegl-0.4/lua/gegl_box-blur.lua
/usr/share/gegl-0.4/lua/gegl_c2g.lua
/usr/share/gegl-0.4/lua/gegl_crop.lua
/usr/share/gegl-0.4/lua/gegl_edge-neon.lua
/usr/share/gegl-0.4/lua/gegl_fill-path.lua
/usr/share/gegl-0.4/lua/gegl_gaussian-blur.lua
/usr/share/gegl-0.4/lua/gegl_linear-gradient.lua
/usr/share/gegl-0.4/lua/gegl_median-blur.lua
/usr/share/gegl-0.4/lua/gegl_radial-gradient.lua
/usr/share/gegl-0.4/lua/gegl_rectangle.lua
/usr/share/gegl-0.4/lua/gegl_rotate.lua
/usr/share/gegl-0.4/lua/gegl_snn-mean.lua
/usr/share/gegl-0.4/lua/gegl_stress.lua
/usr/share/gegl-0.4/lua/gegl_translate.lua
/usr/share/gegl-0.4/lua/gegl_unsharp-mask.lua
/usr/share/gegl-0.4/lua/gegl_vector-stroke.lua
/usr/share/gegl-0.4/lua/init.lua
/usr/share/gegl-0.4/lua/mime.lua
/usr/share/gegl-0.4/lua/mrg.lua
/usr/share/gegl-0.4/lua/mrl.lua
/usr/share/gegl-0.4/lua/preferences.lua
/usr/share/gegl-0.4/lua/viewer.lua
/usr/share/gir-1.0/*.gir

%files dev
%defattr(-,root,root,-)
/usr/include/gegl-0.4/gegl-apply.h
/usr/include/gegl-0.4/gegl-audio-fragment.h
/usr/include/gegl-0.4/gegl-buffer-backend.h
/usr/include/gegl-0.4/gegl-buffer-enums.h
/usr/include/gegl-0.4/gegl-buffer-iterator.h
/usr/include/gegl-0.4/gegl-buffer-matrix2.h
/usr/include/gegl-0.4/gegl-buffer-swap.h
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
/usr/include/gegl-0.4/gegl-memory.h
/usr/include/gegl-0.4/gegl-node.h
/usr/include/gegl-0.4/gegl-op.h
/usr/include/gegl-0.4/gegl-operations-util.h
/usr/include/gegl-0.4/gegl-parallel.h
/usr/include/gegl-0.4/gegl-paramspecs.h
/usr/include/gegl-0.4/gegl-path.h
/usr/include/gegl-0.4/gegl-plugin.h
/usr/include/gegl-0.4/gegl-processor.h
/usr/include/gegl-0.4/gegl-random.h
/usr/include/gegl-0.4/gegl-rectangle.h
/usr/include/gegl-0.4/gegl-scratch.h
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
/usr/lib64/gegl-0.4/exr-load.so
/usr/lib64/gegl-0.4/exr-save.so
/usr/lib64/gegl-0.4/ff-load.so
/usr/lib64/gegl-0.4/ff-save.so
/usr/lib64/gegl-0.4/gegl-common-cxx.so
/usr/lib64/gegl-0.4/gegl-common-gpl3.so
/usr/lib64/gegl-0.4/gegl-common.so
/usr/lib64/gegl-0.4/gegl-core.so
/usr/lib64/gegl-0.4/gegl-generated.so
/usr/lib64/gegl-0.4/gif-load.so
/usr/lib64/gegl-0.4/jpg-load.so
/usr/lib64/gegl-0.4/jpg-save.so
/usr/lib64/gegl-0.4/lcms-from-profile.so
/usr/lib64/gegl-0.4/npd.so
/usr/lib64/gegl-0.4/npy-save.so
/usr/lib64/gegl-0.4/path.so
/usr/lib64/gegl-0.4/pixbuf-load.so
/usr/lib64/gegl-0.4/pixbuf-save.so
/usr/lib64/gegl-0.4/png-load.so
/usr/lib64/gegl-0.4/png-save.so
/usr/lib64/gegl-0.4/ppm-load.so
/usr/lib64/gegl-0.4/ppm-save.so
/usr/lib64/gegl-0.4/raw-load.so
/usr/lib64/gegl-0.4/rgbe-load.so
/usr/lib64/gegl-0.4/rgbe-save.so
/usr/lib64/gegl-0.4/sdl2-display.so
/usr/lib64/gegl-0.4/seamless-clone-compose.so
/usr/lib64/gegl-0.4/seamless-clone.so
/usr/lib64/gegl-0.4/svg-load.so
/usr/lib64/gegl-0.4/text.so
/usr/lib64/gegl-0.4/transformops.so
/usr/lib64/gegl-0.4/v4l.so
/usr/lib64/gegl-0.4/vector-fill.so
/usr/lib64/gegl-0.4/vector-stroke.so
/usr/lib64/gegl-0.4/webp-load.so
/usr/lib64/gegl-0.4/webp-save.so
/usr/lib64/libgegl-0.4.so
/usr/lib64/libgegl-0.4.so.0
/usr/lib64/libgegl-0.4.so.0.419.1
/usr/lib64/libgegl-npd-0.4.so
/usr/lib64/libgegl-sc-0.4.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gegl/178f030d76bde249653291b58a7e8066755051be
/usr/share/package-licenses/gegl/7181028b2cb15912d89c76ca33b720a3bfb537cc
/usr/share/package-licenses/gegl/7cd64aeec55f96676d9e34b6b1677ec470e45fcf
/usr/share/package-licenses/gegl/855d3492027e24b96cc759b7fa729176cb1bdca7
/usr/share/package-licenses/gegl/91664a5e5a2b5bf020a621d0e9c5cc507e619c94
/usr/share/package-licenses/gegl/e7d563f52bf5295e6dba1d67ac23e9f6a160fab9

%files locales -f gegl-0.4.lang
%defattr(-,root,root,-)

