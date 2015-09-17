// ┌─────────────────────────────────────────────────────────────────────┐ \\
// │ Raphaël 2.0.1 - JavaScript Vector Library                           │ \\
// ├─────────────────────────────────────────────────────────────────────┤ \\
// │ Copyright (c) 2008-2011 Dmitry Baranovskiy (http://raphaeljs.com)   │ \\
// │ Copyright (c) 2008-2011 Sencha Labs (http://sencha.com)             │ \\
// │ Licensed under the MIT (http://raphaeljs.com/license.html) license. │ \\
// └─────────────────────────────────────────────────────────────────────┘ \\
(function (a) {
    var b = "0.4.0", c = "hasOwnProperty", d = /[\.\/]/, e = "*", f = function () {
    }, g = function (a, b) {
        return a - b
    }, h, i, j = {n: {}}, k = function (a, b) {
        var c = j, d = i, e = Array.prototype.slice.call(arguments, 2), f = k.listeners(a), l = 0, m = !1, n, o = [], p = {}, q = [], r = [];
        h = a, i = 0;
        for (var s = 0, t = f.length; s < t; s++)"zIndex"in f[s] && (o.push(f[s].zIndex), f[s].zIndex < 0 && (p[f[s].zIndex] = f[s]));
        o.sort(g);
        while (o[l] < 0) {
            n = p[o[l++]], q.push(n.apply(b, e));
            if (i) {
                i = d;
                return q
            }
        }
        for (s = 0; s < t; s++) {
            n = f[s];
            if ("zIndex"in n)if (n.zIndex == o[l]) {
                q.push(n.apply(b, e));
                if (i) {
                    i = d;
                    return q
                }
                do {
                    l++, n = p[o[l]], n && q.push(n.apply(b, e));
                    if (i) {
                        i = d;
                        return q
                    }
                } while (n)
            } else p[n.zIndex] = n; else {
                q.push(n.apply(b, e));
                if (i) {
                    i = d;
                    return q
                }
            }
        }
        i = d;
        return q.length ? q : null
    };
    k.listeners = function (a) {
        var b = a.split(d), c = j, f, g, h, i, k, l, m, n, o = [c], p = [];
        for (i = 0, k = b.length; i < k; i++) {
            n = [];
            for (l = 0, m = o.length; l < m; l++) {
                c = o[l].n, g = [c[b[i]], c[e]], h = 2;
                while (h--)f = g[h], f && (n.push(f), p = p.concat(f.f || []))
            }
            o = n
        }
        return p
    }, k.on = function (a, b) {
        var c = a.split(d), e = j;
        for (var g = 0, h = c.length; g < h; g++)e = e.n, !e[c[g]] && (e[c[g]] = {n: {}}), e = e[c[g]];
        e.f = e.f || [];
        for (g = 0, h = e.f.length; g < h; g++)if (e.f[g] == b)return f;
        e.f.push(b);
        return function (a) {
            +a == +a && (b.zIndex = +a)
        }
    }, k.stop = function () {
        i = 1
    }, k.nt = function (a) {
        if (a)return (new RegExp("(?:\\.|\\/|^)" + a + "(?:\\.|\\/|$)")).test(h);
        return h
    }, k.unbind = function (a, b) {
        var f = a.split(d), g, h, i, k, l, m, n, o = [j];
        for (k = 0, l = f.length; k < l; k++)for (m = 0; m < o.length; m += i.length - 2) {
            i = [m, 1], g = o[m].n;
            if (f[k] != e)g[f[k]] && i.push(g[f[k]]); else for (h in g)g[c](h) && i.push(g[h]);
            o.splice.apply(o, i)
        }
        for (k = 0, l = o.length; k < l; k++) {
            g = o[k];
            while (g.n) {
                if (b) {
                    if (g.f) {
                        for (m = 0, n = g.f.length; m < n; m++)if (g.f[m] == b) {
                            g.f.splice(m, 1);
                            break
                        }
                        !g.f.length && delete g.f
                    }
                    for (h in g.n)if (g.n[c](h) && g.n[h].f) {
                        var p = g.n[h].f;
                        for (m = 0, n = p.length; m < n; m++)if (p[m] == b) {
                            p.splice(m, 1);
                            break
                        }
                        !p.length && delete g.n[h].f
                    }
                } else {
                    delete g.f;
                    for (h in g.n)g.n[c](h) && g.n[h].f && delete g.n[h].f
                }
                g = g.n
            }
        }
    }, k.once = function (a, b) {
        var c = function () {
            b.apply(this, arguments), k.unbind(a, c)
        };
        return k.on(a, c)
    }, k.version = b, k.toString = function () {
        return "You are running Eve " + b
    }, typeof module != "undefined" && module.exports ? module.exports = k : a.eve = k
})(this), function () {
    function cr(b, d, e, f, h, i) {
        e = Q(e);
        var j, k, l, m = [], o, p, q, t = b.ms, u = {}, v = {}, w = {};
        if (f)for (y = 0, z = cl.length; y < z; y++) {
            var x = cl[y];
            if (x.el.id == d.id && x.anim == b) {
                x.percent != e ? (cl.splice(y, 1), l = 1) : k = x, d.attr(x.totalOrigin);
                break
            }
        } else f = +v;
        for (var y = 0, z = b.percents.length; y < z; y++) {
            if (b.percents[y] == e || b.percents[y] > f * b.top) {
                e = b.percents[y], p = b.percents[y - 1] || 0, t = t / b.top * (e - p), o = b.percents[y + 1], j = b.anim[e];
                break
            }
            f && d.attr(b.anim[b.percents[y]])
        }
        if (!!j) {
            if (!k) {
                for (var A in j)if (j[g](A))if (U[g](A) || d.paper.customAttributes[g](A)) {
                    u[A] = d.attr(A), u[A] == null && (u[A] = T[A]), v[A] = j[A];
                    switch (U[A]) {
                        case C:
                            w[A] = (v[A] - u[A]) / t;
                            break;
                        case"colour":
                            u[A] = a.getRGB(u[A]);
                            var B = a.getRGB(v[A]);
                            w[A] = {r: (B.r - u[A].r) / t, g: (B.g - u[A].g) / t, b: (B.b - u[A].b) / t};
                            break;
                        case"path":
                            var D = bG(u[A], v[A]), E = D[1];
                            u[A] = D[0], w[A] = [];
                            for (y = 0, z = u[A].length; y < z; y++) {
                                w[A][y] = [0];
                                for (var F = 1, G = u[A][y].length; F < G; F++)w[A][y][F] = (E[y][F] - u[A][y][F]) / t
                            }
                            break;
                        case"transform":
                            var H = d._, I = bP(H[A], v[A]);
                            if (I) {
                                u[A] = I.from, v[A] = I.to, w[A] = [], w[A].real = !0;
                                for (y = 0, z = u[A].length; y < z; y++) {
                                    w[A][y] = [u[A][y][0]];
                                    for (F = 1, G = u[A][y].length; F < G; F++)w[A][y][F] = (v[A][y][F] - u[A][y][F]) / t
                                }
                            } else {
                                var J = d.matrix || new bQ, K = {
                                    _: {transform: H.transform}, getBBox: function () {
                                        return d.getBBox(1)
                                    }
                                };
                                u[A] = [J.a, J.b, J.c, J.d, J.e, J.f], bN(K, v[A]), v[A] = K._.transform, w[A] = [(K.matrix.a - J.a) / t, (K.matrix.b - J.b) / t, (K.matrix.c - J.c) / t, (K.matrix.d - J.d) / t, (K.matrix.e - J.e) / t, (K.matrix.e - J.f) / t]
                            }
                            break;
                        case"csv":
                            var L = r(j[A])[s](c), M = r(u[A])[s](c);
                            if (A == "clip-rect") {
                                u[A] = M, w[A] = [], y = M.length;
                                while (y--)w[A][y] = (L[y] - u[A][y]) / t
                            }
                            v[A] = L;
                            break;
                        default:
                            L = [][n](j[A]), M = [][n](u[A]), w[A] = [], y = d.paper.customAttributes[A].length;
                            while (y--)w[A][y] = ((L[y] || 0) - (M[y] || 0)) / t
                    }
                }
                var O = j.easing, P = a.easing_formulas[O];
                if (!P) {
                    P = r(O).match(N);
                    if (P && P.length == 5) {
                        var R = P;
                        P = function (a) {
                            return cp(a, +R[1], +R[2], +R[3], +R[4], t)
                        }
                    } else P = be
                }
                q = j.start || b.start || +(new Date), x = {
                    anim: b,
                    percent: e,
                    timestamp: q,
                    start: q + (b.del || 0),
                    status: 0,
                    initstatus: f || 0,
                    stop: !1,
                    ms: t,
                    easing: P,
                    from: u,
                    diff: w,
                    to: v,
                    el: d,
                    callback: j.callback,
                    prev: p,
                    next: o,
                    repeat: i || b.times,
                    origin: d.attr(),
                    totalOrigin: h
                }, cl.push(x);
                if (f && !k && !l) {
                    x.stop = !0, x.start = new Date - t * f;
                    if (cl.length == 1)return cn()
                }
                l && (x.start = new Date - x.ms * f), cl.length == 1 && cm(cn)
            } else k.initstatus = f, k.start = new Date - k.ms * f;
            eve("anim.start." + d.id, d, b)
        }
    }

    function cq(a, b) {
        var c = [], d = {};
        this.ms = b, this.times = 1;
        if (a) {
            for (var e in a)a[g](e) && (d[Q(e)] = a[e], c.push(Q(e)));
            c.sort(bc)
        }
        this.anim = d, this.top = c[c.length - 1], this.percents = c
    }

    function cp(a, b, c, d, e, f) {
        function o(a, b) {
            var c, d, e, f, j, k;
            for (e = a, k = 0; k < 8; k++) {
                f = m(e) - a;
                if (z(f) < b)return e;
                j = (3 * i * e + 2 * h) * e + g;
                if (z(j) < 1e-6)break;
                e = e - f / j
            }
            c = 0, d = 1, e = a;
            if (e < c)return c;
            if (e > d)return d;
            while (c < d) {
                f = m(e);
                if (z(f - a) < b)return e;
                a > f ? c = e : d = e, e = (d - c) / 2 + c
            }
            return e
        }

        function n(a, b) {
            var c = o(a, b);
            return ((l * c + k) * c + j) * c
        }

        function m(a) {
            return ((i * a + h) * a + g) * a
        }

        var g = 3 * b, h = 3 * (d - b) - g, i = 1 - g - h, j = 3 * c, k = 3 * (e - c) - j, l = 1 - j - k;
        return n(a, 1 / (200 * f))
    }

    function cd() {
        return this.x + q + this.y + q + this.width + " × " + this.height
    }

    function cc() {
        return this.x + q + this.y
    }

    function bQ(a, b, c, d, e, f) {
        a != null ? (this.a = +a, this.b = +b, this.c = +c, this.d = +d, this.e = +e, this.f = +f) : (this.a = 1, this.b = 0, this.c = 0, this.d = 1, this.e = 0, this.f = 0)
    }

    function bw(a) {
        var b = [];
        for (var c = 0, d = a.length; d - 2 > c; c += 2) {
            var e = [{x: +a[c], y: +a[c + 1]}, {x: +a[c], y: +a[c + 1]}, {x: +a[c + 2], y: +a[c + 3]}, {
                x: +a[c + 4],
                y: +a[c + 5]
            }];
            d - 4 == c ? (e[0] = {x: +a[c - 2], y: +a[c - 1]}, e[3] = e[2]) : c && (e[0] = {
                x: +a[c - 2],
                y: +a[c - 1]
            }), b.push(["C", (-e[0].x + 6 * e[1].x + e[2].x) / 6, (-e[0].y + 6 * e[1].y + e[2].y) / 6, (e[1].x + 6 * e[2].x - e[3].x) / 6, (e[1].y + 6 * e[2].y - e[3].y) / 6, e[2].x, e[2].y])
        }
        return b
    }

    function bv() {
        return this.hex
    }

    function bt(a, b, c) {
        function d() {
            var e = Array.prototype.slice.call(arguments, 0), f = e.join("␀"), h = d.cache = d.cache || {}, i = d.count = d.count || [];
            if (h[g](f)) {
                bs(i, f);
                return c ? c(h[f]) : h[f]
            }
            i.length >= 1e3 && delete h[i.shift()], i.push(f), h[f] = a[m](b, e);
            return c ? c(h[f]) : h[f]
        }

        return d
    }

    function bs(a, b) {
        for (var c = 0, d = a.length; c < d; c++)if (a[c] === b)return a.push(a.splice(c, 1)[0])
    }

    function a(c) {
        if (a.is(c, "function"))return b ? c() : eve.on("DOMload", c);
        if (a.is(c, E))return a._engine.create[m](a, c.splice(0, 3 + a.is(c[0], C))).add(c);
        var d = Array.prototype.slice.call(arguments, 0);
        if (a.is(d[d.length - 1], "function")) {
            var e = d.pop();
            return b ? e.call(a._engine.create[m](a, d)) : eve.on("DOMload", function () {
                e.call(a._engine.create[m](a, d))
            })
        }
        return a._engine.create[m](a, arguments)
    }

    a.version = "2.0.1", a.eve = eve;
    var b, c = /[, ]+/, d = {
        circle: 1,
        rect: 1,
        path: 1,
        ellipse: 1,
        text: 1,
        image: 1
    }, e = /\{(\d+)\}/g, f = "prototype", g = "hasOwnProperty", h = {
        doc: document,
        win: window
    }, i = {was: Object.prototype[g].call(h.win, "Raphael"), is: h.win.Raphael}, j = function () {
        this.ca = this.customAttributes = {}
    }, k, l = "appendChild", m = "apply", n = "concat", o = "createTouch"in h.doc, p = "", q = " ", r = String, s = "split", t = "click dblclick mousedown mousemove mouseout mouseover mouseup touchstart touchmove touchend touchcancel"[s](q), u = {
        mousedown: "touchstart",
        mousemove: "touchmove",
        mouseup: "touchend"
    }, v = r.prototype.toLowerCase, w = Math, x = w.max, y = w.min, z = w.abs, A = w.pow, B = w.PI, C = "number", D = "string", E = "array", F = "toString", G = "fill", H = Object.prototype.toString, I = {}, J = "push", K = a._ISURL = /^url\(['"]?([^\)]+?)['"]?\)$/i, L = /^\s*((#[a-f\d]{6})|(#[a-f\d]{3})|rgba?\(\s*([\d\.]+%?\s*,\s*[\d\.]+%?\s*,\s*[\d\.]+%?(?:\s*,\s*[\d\.]+%?)?)\s*\)|hsba?\(\s*([\d\.]+(?:deg|\xb0|%)?\s*,\s*[\d\.]+%?\s*,\s*[\d\.]+(?:%?\s*,\s*[\d\.]+)?)%?\s*\)|hsla?\(\s*([\d\.]+(?:deg|\xb0|%)?\s*,\s*[\d\.]+%?\s*,\s*[\d\.]+(?:%?\s*,\s*[\d\.]+)?)%?\s*\))\s*$/i, M = {
        NaN: 1,
        Infinity: 1,
        "-Infinity": 1
    }, N = /^(?:cubic-)?bezier\(([^,]+),([^,]+),([^,]+),([^\)]+)\)/, O = w.round, P = "setAttribute", Q = parseFloat, R = parseInt, S = r.prototype.toUpperCase, T = a._availableAttrs = {
        "arrow-end": "none",
        "arrow-start": "none",
        blur: 0,
        "clip-rect": "0 0 1e9 1e9",
        cursor: "default",
        cx: 0,
        cy: 0,
        fill: "#fff",
        "fill-opacity": 1,
        font: '10px "Arial"',
        "font-family": '"Arial"',
        "font-size": "10",
        "font-style": "normal",
        "font-weight": 400,
        gradient: 0,
        height: 0,
        href: "http://raphaeljs.com/",
        "letter-spacing": 0,
        opacity: 1,
        path: "M0,0",
        r: 0,
        rx: 0,
        ry: 0,
        src: "",
        stroke: "#000",
        "stroke-dasharray": "",
        "stroke-linecap": "butt",
        "stroke-linejoin": "butt",
        "stroke-miterlimit": 0,
        "stroke-opacity": 1,
        "stroke-width": 1,
        target: "_blank",
        "text-anchor": "middle",
        title: "Raphael",
        transform: "",
        width: 0,
        x: 0,
        y: 0
    }, U = a._availableAnimAttrs = {
        blur: C,
        "clip-rect": "csv",
        cx: C,
        cy: C,
        fill: "colour",
        "fill-opacity": C,
        "font-size": C,
        height: C,
        opacity: C,
        path: "path",
        r: C,
        rx: C,
        ry: C,
        stroke: "colour",
        "stroke-opacity": C,
        "stroke-width": C,
        transform: "transform",
        width: C,
        x: C,
        y: C
    }, V = /\s*,\s*/, W = {
        hs: 1,
        rg: 1
    }, X = /,?([achlmqrstvxz]),?/gi, Y = /([achlmrqstvz])[\s,]*((-?\d*\.?\d*(?:e[\-+]?\d+)?\s*,?\s*)+)/ig, Z = /([rstm])[\s,]*((-?\d*\.?\d*(?:e[\-+]?\d+)?\s*,?\s*)+)/ig, $ = /(-?\d*\.?\d*(?:e[\-+]?\d+)?)\s*,?\s*/ig, _ = a._radial_gradient = /^r(?:\(([^,]+?)\s*,\s*([^\)]+?)\))?/, ba = {}, bb = function (a, b) {
        return a.key - b.key
    }, bc = function (a, b) {
        return Q(a) - Q(b)
    }, bd = function () {
    }, be = function (a) {
        return a
    }, bf = a._rectPath = function (a, b, c, d, e) {
        if (e)return [["M", a + e, b], ["l", c - e * 2, 0], ["a", e, e, 0, 0, 1, e, e], ["l", 0, d - e * 2], ["a", e, e, 0, 0, 1, -e, e], ["l", e * 2 - c, 0], ["a", e, e, 0, 0, 1, -e, -e], ["l", 0, e * 2 - d], ["a", e, e, 0, 0, 1, e, -e], ["z"]];
        return [["M", a, b], ["l", c, 0], ["l", 0, d], ["l", -c, 0], ["z"]]
    }, bg = function (a, b, c, d) {
        d == null && (d = c);
        return [["M", a, b], ["m", 0, -d], ["a", c, d, 0, 1, 1, 0, 2 * d], ["a", c, d, 0, 1, 1, 0, -2 * d], ["z"]]
    }, bh = a._getPath = {
        path: function (a) {
            return a.attr("path")
        }, circle: function (a) {
            var b = a.attrs;
            return bg(b.cx, b.cy, b.r)
        }, ellipse: function (a) {
            var b = a.attrs;
            return bg(b.cx, b.cy, b.rx, b.ry)
        }, rect: function (a) {
            var b = a.attrs;
            return bf(b.x, b.y, b.width, b.height, b.r)
        }, image: function (a) {
            var b = a.attrs;
            return bf(b.x, b.y, b.width, b.height)
        }, text: function (a) {
            var b = a._getBBox();
            return bf(b.x, b.y, b.width, b.height)
        }
    }, bi = a.mapPath = function (a, b) {
        if (!b)return a;
        var c, d, e, f, g, h, i;
        a = bG(a);
        for (e = 0, g = a.length; e < g; e++) {
            i = a[e];
            for (f = 1, h = i.length; f < h; f += 2)c = b.x(i[f], i[f + 1]), d = b.y(i[f], i[f + 1]), i[f] = c, i[f + 1] = d
        }
        return a
    };
    a._g = h, a.type = h.win.SVGAngle || h.doc.implementation.hasFeature("http://www.w3.org/TR/SVG11/feature#BasicStructure", "1.1") ? "SVG" : "VML";
    if (a.type == "VML") {
        var bj = h.doc.createElement("div"), bk;
        bj.innerHTML = '<v:shape adj="1"/>', bk = bj.firstChild, bk.style.behavior = "url(#default#VML)";
        if (!bk || typeof bk.adj != "object")return a.type = p;
        bj = null
    }
    a.svg = !(a.vml = a.type == "VML"), a._Paper = j, a.fn = k = j.prototype = a.prototype, a._id = 0, a._oid = 0, a.is = function (a, b) {
        b = v.call(b);
        if (b == "finite")return !M[g](+a);
        if (b == "array")return a instanceof Array;
        return b == "null" && a === null || b == typeof a && a !== null || b == "object" && a === Object(a) || b == "array" && Array.isArray && Array.isArray(a) || H.call(a).slice(8, -1).toLowerCase() == b
    }, a.angle = function (b, c, d, e, f, g) {
        if (f == null) {
            var h = b - d, i = c - e;
            if (!h && !i)return 0;
            return (180 + w.atan2(-i, -h) * 180 / B + 360) % 360
        }
        return a.angle(b, c, f, g) - a.angle(d, e, f, g)
    }, a.rad = function (a) {
        return a % 360 * B / 180
    }, a.deg = function (a) {
        return a * 180 / B % 360
    }, a.snapTo = function (b, c, d) {
        d = a.is(d, "finite") ? d : 10;
        if (a.is(b, E)) {
            var e = b.length;
            while (e--)if (z(b[e] - c) <= d)return b[e]
        } else {
            b = +b;
            var f = c % b;
            if (f < d)return c - f;
            if (f > b - d)return c - f + b
        }
        return c
    };
    var bl = a.createUUID = function (a, b) {
        return function () {
            return "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(a, b).toUpperCase()
        }
    }(/[xy]/g, function (a) {
        var b = w.random() * 16 | 0, c = a == "x" ? b : b & 3 | 8;
        return c.toString(16)
    });
    a.setWindow = function (b) {
        eve("setWindow", a, h.win, b), h.win = b, h.doc = h.win.document, a._engine.initWin && a._engine.initWin(h.win)
    };
    var bm = function (b) {
        if (a.vml) {
            var c = /^\s+|\s+$/g, d;
            try {
                var e = new ActiveXObject("htmlfile");
                e.write("<body>"), e.close(), d = e.body
            } catch (f) {
                d = createPopup().document.body
            }
            var g = d.createTextRange();
            bm = bt(function (a) {
                try {
                    d.style.color = r(a).replace(c, p);
                    var b = g.queryCommandValue("ForeColor");
                    b = (b & 255) << 16 | b & 65280 | (b & 16711680) >>> 16;
                    return "#" + ("000000" + b.toString(16)).slice(-6)
                } catch (e) {
                    return "none"
                }
            })
        } else {
            var i = h.doc.createElement("i");
            i.title = "Raphaël Colour Picker", i.style.display = "none", h.doc.body.appendChild(i), bm = bt(function (a) {
                i.style.color = a;
                return h.doc.defaultView.getComputedStyle(i, p).getPropertyValue("color")
            })
        }
        return bm(b)
    }, bn = function () {
        return "hsb(" + [this.h, this.s, this.b] + ")"
    }, bo = function () {
        return "hsl(" + [this.h, this.s, this.l] + ")"
    }, bp = function () {
        return this.hex
    }, bq = function (b, c, d) {
        c == null && a.is(b, "object") && "r"in b && "g"in b && "b"in b && (d = b.b, c = b.g, b = b.r);
        if (c == null && a.is(b, D)) {
            var e = a.getRGB(b);
            b = e.r, c = e.g, d = e.b
        }
        if (b > 1 || c > 1 || d > 1)b /= 255, c /= 255, d /= 255;
        return [b, c, d]
    }, br = function (b, c, d, e) {
        b *= 255, c *= 255, d *= 255;
        var f = {r: b, g: c, b: d, hex: a.rgb(b, c, d), toString: bp};
        a.is(e, "finite") && (f.opacity = e);
        return f
    };
    a.color = function (b) {
        var c;
        a.is(b, "object") && "h"in b && "s"in b && "b"in b ? (c = a.hsb2rgb(b), b.r = c.r, b.g = c.g, b.b = c.b, b.hex = c.hex) : a.is(b, "object") && "h"in b && "s"in b && "l"in b ? (c = a.hsl2rgb(b), b.r = c.r, b.g = c.g, b.b = c.b, b.hex = c.hex) : (a.is(b, "string") && (b = a.getRGB(b)), a.is(b, "object") && "r"in b && "g"in b && "b"in b ? (c = a.rgb2hsl(b), b.h = c.h, b.s = c.s, b.l = c.l, c = a.rgb2hsb(b), b.v = c.b) : (b = {hex: "none"}, b.r = b.g = b.b = b.h = b.s = b.v = b.l = -1)), b.toString = bp;
        return b
    }, a.hsb2rgb = function (a, b, c, d) {
        this.is(a, "object") && "h"in a && "s"in a && "b"in a && (c = a.b, b = a.s, a = a.h, d = a.o), a *= 360;
        var e, f, g, h, i;
        a = a % 360 / 60, i = c * b, h = i * (1 - z(a % 2 - 1)), e = f = g = c - i, a = ~~a, e += [i, h, 0, 0, h, i][a], f += [h, i, i, h, 0, 0][a], g += [0, 0, h, i, i, h][a];
        return br(e, f, g, d)
    }, a.hsl2rgb = function (a, b, c, d) {
        this.is(a, "object") && "h"in a && "s"in a && "l"in a && (c = a.l, b = a.s, a = a.h);
        if (a > 1 || b > 1 || c > 1)a /= 360, b /= 100, c /= 100;
        a *= 360;
        var e, f, g, h, i;
        a = a % 360 / 60, i = 2 * b * (c < .5 ? c : 1 - c), h = i * (1 - z(a % 2 - 1)), e = f = g = c - i / 2, a = ~~a, e += [i, h, 0, 0, h, i][a], f += [h, i, i, h, 0, 0][a], g += [0, 0, h, i, i, h][a];
        return br(e, f, g, d)
    }, a.rgb2hsb = function (a, b, c) {
        c = bq(a, b, c), a = c[0], b = c[1], c = c[2];
        var d, e, f, g;
        f = x(a, b, c), g = f - y(a, b, c), d = g == 0 ? null : f == a ? (b - c) / g : f == b ? (c - a) / g + 2 : (a - b) / g + 4, d = (d + 360) % 6 * 60 / 360, e = g == 0 ? 0 : g / f;
        return {h: d, s: e, b: f, toString: bn}
    }, a.rgb2hsl = function (a, b, c) {
        c = bq(a, b, c), a = c[0], b = c[1], c = c[2];
        var d, e, f, g, h, i;
        g = x(a, b, c), h = y(a, b, c), i = g - h, d = i == 0 ? null : g == a ? (b - c) / i : g == b ? (c - a) / i + 2 : (a - b) / i + 4, d = (d + 360) % 6 * 60 / 360, f = (g + h) / 2, e = i == 0 ? 0 : f < .5 ? i / (2 * f) : i / (2 - 2 * f);
        return {h: d, s: e, l: f, toString: bo}
    }, a._path2string = function () {
        return this.join(",").replace(X, "$1")
    };
    var bu = a._preload = function (a, b) {
        var c = h.doc.createElement("img");
        c.style.cssText = "position:absolute;left:-9999em;top:-9999em", c.onload = function () {
            b.call(this), this.onload = null, h.doc.body.removeChild(this)
        }, c.onerror = function () {
            h.doc.body.removeChild(this)
        }, h.doc.body.appendChild(c), c.src = a
    };
    a.getRGB = bt(function (b) {
        if (!b || !!((b = r(b)).indexOf("-") + 1))return {r: -1, g: -1, b: -1, hex: "none", error: 1, toString: bv};
        if (b == "none")return {r: -1, g: -1, b: -1, hex: "none", toString: bv};
        !W[g](b.toLowerCase().substring(0, 2)) && b.charAt() != "#" && (b = bm(b));
        var c, d, e, f, h, i, j, k = b.match(L);
        if (k) {
            k[2] && (f = R(k[2].substring(5), 16), e = R(k[2].substring(3, 5), 16), d = R(k[2].substring(1, 3), 16)), k[3] && (f = R((i = k[3].charAt(3)) + i, 16), e = R((i = k[3].charAt(2)) + i, 16), d = R((i = k[3].charAt(1)) + i, 16)), k[4] && (j = k[4][s](V), d = Q(j[0]), j[0].slice(-1) == "%" && (d *= 2.55), e = Q(j[1]), j[1].slice(-1) == "%" && (e *= 2.55), f = Q(j[2]), j[2].slice(-1) == "%" && (f *= 2.55), k[1].toLowerCase().slice(0, 4) == "rgba" && (h = Q(j[3])), j[3] && j[3].slice(-1) == "%" && (h /= 100));
            if (k[5]) {
                j = k[5][s](V), d = Q(j[0]), j[0].slice(-1) == "%" && (d *= 2.55), e = Q(j[1]), j[1].slice(-1) == "%" && (e *= 2.55), f = Q(j[2]), j[2].slice(-1) == "%" && (f *= 2.55), (j[0].slice(-3) == "deg" || j[0].slice(-1) == "°") && (d /= 360), k[1].toLowerCase().slice(0, 4) == "hsba" && (h = Q(j[3])), j[3] && j[3].slice(-1) == "%" && (h /= 100);
                return a.hsb2rgb(d, e, f, h)
            }
            if (k[6]) {
                j = k[6][s](V), d = Q(j[0]), j[0].slice(-1) == "%" && (d *= 2.55), e = Q(j[1]), j[1].slice(-1) == "%" && (e *= 2.55), f = Q(j[2]), j[2].slice(-1) == "%" && (f *= 2.55), (j[0].slice(-3) == "deg" || j[0].slice(-1) == "°") && (d /= 360), k[1].toLowerCase().slice(0, 4) == "hsla" && (h = Q(j[3])), j[3] && j[3].slice(-1) == "%" && (h /= 100);
                return a.hsl2rgb(d, e, f, h)
            }
            k = {
                r: d,
                g: e,
                b: f,
                toString: bv
            }, k.hex = "#" + (16777216 | f | e << 8 | d << 16).toString(16).slice(1), a.is(h, "finite") && (k.opacity = h);
            return k
        }
        return {r: -1, g: -1, b: -1, hex: "none", error: 1, toString: bv}
    }, a), a.hsb = bt(function (b, c, d) {
        return a.hsb2rgb(b, c, d).hex
    }), a.hsl = bt(function (b, c, d) {
        return a.hsl2rgb(b, c, d).hex
    }), a.rgb = bt(function (a, b, c) {
        return "#" + (16777216 | c | b << 8 | a << 16).toString(16).slice(1)
    }), a.getColor = function (a) {
        var b = this.getColor.start = this.getColor.start || {h: 0, s: 1, b: a || .75}, c = this.hsb2rgb(b.h, b.s, b.b);
        b.h += .075, b.h > 1 && (b.h = 0, b.s -= .2, b.s <= 0 && (this.getColor.start = {h: 0, s: 1, b: b.b}));
        return c.hex
    }, a.getColor.reset = function () {
        delete this.start
    }, a.parsePathString = bt(function (b) {
        if (!b)return null;
        var c = {a: 7, c: 6, h: 1, l: 2, m: 2, r: 4, q: 4, s: 4, t: 2, v: 1, z: 0}, d = [];
        a.is(b, E) && a.is(b[0], E) && (d = by(b)), d.length || r(b).replace(Y, function (a, b, e) {
            var f = [], g = b.toLowerCase();
            e.replace($, function (a, b) {
                b && f.push(+b)
            }), g == "m" && f.length > 2 && (d.push([b][n](f.splice(0, 2))), g = "l", b = b == "m" ? "l" : "L");
            if (g == "r")d.push([b][n](f)); else while (f.length >= c[g]) {
                d.push([b][n](f.splice(0, c[g])));
                if (!c[g])break
            }
        }), d.toString = a._path2string;
        return d
    }), a.parseTransformString = bt(function (b) {
        if (!b)return null;
        var c = {r: 3, s: 4, t: 2, m: 6}, d = [];
        a.is(b, E) && a.is(b[0], E) && (d = by(b)), d.length || r(b).replace(Z, function (a, b, c) {
            var e = [], f = v.call(b);
            c.replace($, function (a, b) {
                b && e.push(+b)
            }), d.push([b][n](e))
        }), d.toString = a._path2string;
        return d
    }), a.findDotsAtSegment = function (a, b, c, d, e, f, g, h, i) {
        var j = 1 - i, k = A(j, 3), l = A(j, 2), m = i * i, n = m * i, o = k * a + l * 3 * i * c + j * 3 * i * i * e + n * g, p = k * b + l * 3 * i * d + j * 3 * i * i * f + n * h, q = a + 2 * i * (c - a) + m * (e - 2 * c + a), r = b + 2 * i * (d - b) + m * (f - 2 * d + b), s = c + 2 * i * (e - c) + m * (g - 2 * e + c), t = d + 2 * i * (f - d) + m * (h - 2 * f + d), u = j * a + i * c, v = j * b + i * d, x = j * e + i * g, y = j * f + i * h, z = 90 - w.atan2(q - s, r - t) * 180 / B;
        (q > s || r < t) && (z += 180);
        return {x: o, y: p, m: {x: q, y: r}, n: {x: s, y: t}, start: {x: u, y: v}, end: {x: x, y: y}, alpha: z}
    }, a._removedFactory = function (a) {
        return function () {
            throw new Error("Raphaël: you are calling to method “" + a + "” of removed object")
        }
    };
    var bx = bt(function (a) {
        if (!a)return {x: 0, y: 0, width: 0, height: 0};
        a = bG(a);
        var b = 0, c = 0, d = [], e = [], f;
        for (var g = 0, h = a.length; g < h; g++) {
            f = a[g];
            if (f[0] == "M")b = f[1], c = f[2], d.push(b), e.push(c); else {
                var i = bF(b, c, f[1], f[2], f[3], f[4], f[5], f[6]);
                d = d[n](i.min.x, i.max.x), e = e[n](i.min.y, i.max.y), b = f[5], c = f[6]
            }
        }
        var j = y[m](0, d), k = y[m](0, e);
        return {x: j, y: k, width: x[m](0, d) - j, height: x[m](0, e) - k}
    }, null, function (a) {
        return {x: a.x, y: a.y, width: a.width, height: a.height}
    }), by = function (b) {
        var c = [];
        if (!a.is(b, E) || !a.is(b && b[0], E))b = a.parsePathString(b);
        for (var d = 0, e = b.length; d < e; d++) {
            c[d] = [];
            for (var f = 0, g = b[d].length; f < g; f++)c[d][f] = b[d][f]
        }
        c.toString = a._path2string;
        return c
    }, bz = a._pathToRelative = bt(function (b) {
        if (!a.is(b, E) || !a.is(b && b[0], E))b = a.parsePathString(b);
        var c = [], d = 0, e = 0, f = 0, g = 0, h = 0;
        b[0][0] == "M" && (d = b[0][1], e = b[0][2], f = d, g = e, h++, c.push(["M", d, e]));
        for (var i = h, j = b.length; i < j; i++) {
            var k = c[i] = [], l = b[i];
            if (l[0] != v.call(l[0])) {
                k[0] = v.call(l[0]);
                switch (k[0]) {
                    case"a":
                        k[1] = l[1], k[2] = l[2], k[3] = l[3], k[4] = l[4], k[5] = l[5], k[6] = +(l[6] - d).toFixed(3), k[7] = +(l[7] - e).toFixed(3);
                        break;
                    case"v":
                        k[1] = +(l[1] - e).toFixed(3);
                        break;
                    case"m":
                        f = l[1], g = l[2];
                    default:
                        for (var m = 1, n = l.length; m < n; m++)k[m] = +(l[m] - (m % 2 ? d : e)).toFixed(3)
                }
            } else {
                k = c[i] = [], l[0] == "m" && (f = l[1] + d, g = l[2] + e);
                for (var o = 0, p = l.length; o < p; o++)c[i][o] = l[o]
            }
            var q = c[i].length;
            switch (c[i][0]) {
                case"z":
                    d = f, e = g;
                    break;
                case"h":
                    d += +c[i][q - 1];
                    break;
                case"v":
                    e += +c[i][q - 1];
                    break;
                default:
                    d += +c[i][q - 2], e += +c[i][q - 1]
            }
        }
        c.toString = a._path2string;
        return c
    }, 0, by), bA = a._pathToAbsolute = bt(function (b) {
        if (!a.is(b, E) || !a.is(b && b[0], E))b = a.parsePathString(b);
        if (!b || !b.length)return [["M", 0, 0]];
        var c = [], d = 0, e = 0, f = 0, g = 0, h = 0;
        b[0][0] == "M" && (d = +b[0][1], e = +b[0][2], f = d, g = e, h++, c[0] = ["M", d, e]);
        for (var i, j, k = h, l = b.length; k < l; k++) {
            c.push(i = []), j = b[k];
            if (j[0] != S.call(j[0])) {
                i[0] = S.call(j[0]);
                switch (i[0]) {
                    case"A":
                        i[1] = j[1], i[2] = j[2], i[3] = j[3], i[4] = j[4], i[5] = j[5], i[6] = +(j[6] + d), i[7] = +(j[7] + e);
                        break;
                    case"V":
                        i[1] = +j[1] + e;
                        break;
                    case"H":
                        i[1] = +j[1] + d;
                        break;
                    case"R":
                        var m = [d, e][n](j.slice(1));
                        for (var o = 2, p = m.length; o < p; o++)m[o] = +m[o] + d, m[++o] = +m[o] + e;
                        c.pop(), c = c[n](bw(m));
                        break;
                    case"M":
                        f = +j[1] + d, g = +j[2] + e;
                    default:
                        for (o = 1, p = j.length; o < p; o++)i[o] = +j[o] + (o % 2 ? d : e)
                }
            } else if (j[0] == "R")m = [d, e][n](j.slice(1)), c.pop(), c = c[n](bw(m)), i = ["R"][n](j.slice(-2)); else for (var q = 0, r = j.length; q < r; q++)i[q] = j[q];
            switch (i[0]) {
                case"Z":
                    d = f, e = g;
                    break;
                case"H":
                    d = i[1];
                    break;
                case"V":
                    e = i[1];
                    break;
                case"M":
                    f = i[i.length - 2], g = i[i.length - 1];
                default:
                    d = i[i.length - 2], e = i[i.length - 1]
            }
        }
        c.toString = a._path2string;
        return c
    }, null, by), bB = function (a, b, c, d) {
        return [a, b, c, d, c, d]
    }, bC = function (a, b, c, d, e, f) {
        var g = 1 / 3, h = 2 / 3;
        return [g * a + h * c, g * b + h * d, g * e + h * c, g * f + h * d, e, f]
    }, bD = function (a, b, c, d, e, f, g, h, i, j) {
        var k = B * 120 / 180, l = B / 180 * (+e || 0), m = [], o, p = bt(function (a, b, c) {
            var d = a * w.cos(c) - b * w.sin(c), e = a * w.sin(c) + b * w.cos(c);
            return {x: d, y: e}
        });
        if (!j) {
            o = p(a, b, -l), a = o.x, b = o.y, o = p(h, i, -l), h = o.x, i = o.y;
            var q = w.cos(B / 180 * e), r = w.sin(B / 180 * e), t = (a - h) / 2, u = (b - i) / 2, v = t * t / (c * c) + u * u / (d * d);
            v > 1 && (v = w.sqrt(v), c = v * c, d = v * d);
            var x = c * c, y = d * d, A = (f == g ? -1 : 1) * w.sqrt(z((x * y - x * u * u - y * t * t) / (x * u * u + y * t * t))), C = A * c * u / d + (a + h) / 2, D = A * -d * t / c + (b + i) / 2, E = w.asin(((b - D) / d).toFixed(9)), F = w.asin(((i - D) / d).toFixed(9));
            E = a < C ? B - E : E, F = h < C ? B - F : F, E < 0 && (E = B * 2 + E), F < 0 && (F = B * 2 + F), g && E > F && (E = E - B * 2), !g && F > E && (F = F - B * 2)
        } else E = j[0], F = j[1], C = j[2], D = j[3];
        var G = F - E;
        if (z(G) > k) {
            var H = F, I = h, J = i;
            F = E + k * (g && F > E ? 1 : -1), h = C + c * w.cos(F), i = D + d * w.sin(F), m = bD(h, i, c, d, e, 0, g, I, J, [F, H, C, D])
        }
        G = F - E;
        var K = w.cos(E), L = w.sin(E), M = w.cos(F), N = w.sin(F), O = w.tan(G / 4), P = 4 / 3 * c * O, Q = 4 / 3 * d * O, R = [a, b], S = [a + P * L, b - Q * K], T = [h + P * N, i - Q * M], U = [h, i];
        S[0] = 2 * R[0] - S[0], S[1] = 2 * R[1] - S[1];
        if (j)return [S, T, U][n](m);
        m = [S, T, U][n](m).join()[s](",");
        var V = [];
        for (var W = 0, X = m.length; W < X; W++)V[W] = W % 2 ? p(m[W - 1], m[W], l).y : p(m[W], m[W + 1], l).x;
        return V
    }, bE = function (a, b, c, d, e, f, g, h, i) {
        var j = 1 - i;
        return {
            x: A(j, 3) * a + A(j, 2) * 3 * i * c + j * 3 * i * i * e + A(i, 3) * g,
            y: A(j, 3) * b + A(j, 2) * 3 * i * d + j * 3 * i * i * f + A(i, 3) * h
        }
    }, bF = bt(function (a, b, c, d, e, f, g, h) {
        var i = e - 2 * c + a - (g - 2 * e + c), j = 2 * (c - a) - 2 * (e - c), k = a - c, l = (-j + w.sqrt(j * j - 4 * i * k)) / 2 / i, n = (-j - w.sqrt(j * j - 4 * i * k)) / 2 / i, o = [b, h], p = [a, g], q;
        z(l) > "1e12" && (l = .5), z(n) > "1e12" && (n = .5), l > 0 && l < 1 && (q = bE(a, b, c, d, e, f, g, h, l), p.push(q.x), o.push(q.y)), n > 0 && n < 1 && (q = bE(a, b, c, d, e, f, g, h, n), p.push(q.x), o.push(q.y)), i = f - 2 * d + b - (h - 2 * f + d), j = 2 * (d - b) - 2 * (f - d), k = b - d, l = (-j + w.sqrt(j * j - 4 * i * k)) / 2 / i, n = (-j - w.sqrt(j * j - 4 * i * k)) / 2 / i, z(l) > "1e12" && (l = .5), z(n) > "1e12" && (n = .5), l > 0 && l < 1 && (q = bE(a, b, c, d, e, f, g, h, l), p.push(q.x), o.push(q.y)), n > 0 && n < 1 && (q = bE(a, b, c, d, e, f, g, h, n), p.push(q.x), o.push(q.y));
        return {min: {x: y[m](0, p), y: y[m](0, o)}, max: {x: x[m](0, p), y: x[m](0, o)}}
    }), bG = a._path2curve = bt(function (a, b) {
        var c = bA(a), d = b && bA(b), e = {x: 0, y: 0, bx: 0, by: 0, X: 0, Y: 0, qx: null, qy: null}, f = {
            x: 0,
            y: 0,
            bx: 0,
            by: 0,
            X: 0,
            Y: 0,
            qx: null,
            qy: null
        }, g = function (a, b) {
            var c, d;
            if (!a)return ["C", b.x, b.y, b.x, b.y, b.x, b.y];
            !(a[0]in{T: 1, Q: 1}) && (b.qx = b.qy = null);
            switch (a[0]) {
                case"M":
                    b.X = a[1], b.Y = a[2];
                    break;
                case"A":
                    a = ["C"][n](bD[m](0, [b.x, b.y][n](a.slice(1))));
                    break;
                case"S":
                    c = b.x + (b.x - (b.bx || b.x)), d = b.y + (b.y - (b.by || b.y)), a = ["C", c, d][n](a.slice(1));
                    break;
                case"T":
                    b.qx = b.x + (b.x - (b.qx || b.x)), b.qy = b.y + (b.y - (b.qy || b.y)), a = ["C"][n](bC(b.x, b.y, b.qx, b.qy, a[1], a[2]));
                    break;
                case"Q":
                    b.qx = a[1], b.qy = a[2], a = ["C"][n](bC(b.x, b.y, a[1], a[2], a[3], a[4]));
                    break;
                case"L":
                    a = ["C"][n](bB(b.x, b.y, a[1], a[2]));
                    break;
                case"H":
                    a = ["C"][n](bB(b.x, b.y, a[1], b.y));
                    break;
                case"V":
                    a = ["C"][n](bB(b.x, b.y, b.x, a[1]));
                    break;
                case"Z":
                    a = ["C"][n](bB(b.x, b.y, b.X, b.Y))
            }
            return a
        }, h = function (a, b) {
            if (a[b].length > 7) {
                a[b].shift();
                var e = a[b];
                while (e.length)a.splice(b++, 0, ["C"][n](e.splice(0, 6)));
                a.splice(b, 1), k = x(c.length, d && d.length || 0)
            }
        }, i = function (a, b, e, f, g) {
            a && b && a[g][0] == "M" && b[g][0] != "M" && (b.splice(g, 0, ["M", f.x, f.y]), e.bx = 0, e.by = 0, e.x = a[g][1], e.y = a[g][2], k = x(c.length, d && d.length || 0))
        };
        for (var j = 0, k = x(c.length, d && d.length || 0); j < k; j++) {
            c[j] = g(c[j], e), h(c, j), d && (d[j] = g(d[j], f)), d && h(d, j), i(c, d, e, f, j), i(d, c, f, e, j);
            var l = c[j], o = d && d[j], p = l.length, q = d && o.length;
            e.x = l[p - 2], e.y = l[p - 1], e.bx = Q(l[p - 4]) || e.x, e.by = Q(l[p - 3]) || e.y, f.bx = d && (Q(o[q - 4]) || f.x), f.by = d && (Q(o[q - 3]) || f.y), f.x = d && o[q - 2], f.y = d && o[q - 1]
        }
        return d ? [c, d] : c
    }, null, by), bH = a._parseDots = bt(function (b) {
        var c = [];
        for (var d = 0, e = b.length; d < e; d++) {
            var f = {}, g = b[d].match(/^([^:]*):?([\d\.]*)/);
            f.color = a.getRGB(g[1]);
            if (f.color.error)return null;
            f.color = f.color.hex, g[2] && (f.offset = g[2] + "%"), c.push(f)
        }
        for (d = 1, e = c.length - 1; d < e; d++)if (!c[d].offset) {
            var h = Q(c[d - 1].offset || 0), i = 0;
            for (var j = d + 1; j < e; j++)if (c[j].offset) {
                i = c[j].offset;
                break
            }
            i || (i = 100, j = e), i = Q(i);
            var k = (i - h) / (j - d + 1);
            for (; d < j; d++)h += k, c[d].offset = h + "%"
        }
        return c
    }), bI = a._tear = function (a, b) {
        a == b.top && (b.top = a.prev), a == b.bottom && (b.bottom = a.next), a.next && (a.next.prev = a.prev), a.prev && (a.prev.next = a.next)
    }, bJ = a._tofront = function (a, b) {
        b.top !== a && (bI(a, b), a.next = null, a.prev = b.top, b.top.next = a, b.top = a)
    }, bK = a._toback = function (a, b) {
        b.bottom !== a && (bI(a, b), a.next = b.bottom, a.prev = null, b.bottom.prev = a, b.bottom = a)
    }, bL = a._insertafter = function (a, b, c) {
        bI(a, c), b == c.top && (c.top = a), b.next && (b.next.prev = a), a.next = b.next, a.prev = b, b.next = a
    }, bM = a._insertbefore = function (a, b, c) {
        bI(a, c), b == c.bottom && (c.bottom = a), b.prev && (b.prev.next = a), a.prev = b.prev, b.prev = a, a.next = b
    }, bN = a._extractTransform = function (b, c) {
        if (c == null)return b._.transform;
        c = r(c).replace(/\.{3}|\u2026/g, b._.transform || p);
        var d = a.parseTransformString(c), e = 0, f = 0, g = 0, h = 1, i = 1, j = b._, k = new bQ;
        j.transform = d || [];
        if (d)for (var l = 0, m = d.length; l < m; l++) {
            var n = d[l], o = n.length, q = r(n[0]).toLowerCase(), s = n[0] != q, t = s ? k.invert() : 0, u, v, w, x, y;
            q == "t" && o == 3 ? s ? (u = t.x(0, 0), v = t.y(0, 0), w = t.x(n[1], n[2]), x = t.y(n[1], n[2]), k.translate(w - u, x - v)) : k.translate(n[1], n[2]) : q == "r" ? o == 2 ? (y = y || b.getBBox(1), k.rotate(n[1], y.x + y.width / 2, y.y + y.height / 2), e += n[1]) : o == 4 && (s ? (w = t.x(n[2], n[3]), x = t.y(n[2], n[3]), k.rotate(n[1], w, x)) : k.rotate(n[1], n[2], n[3]), e += n[1]) : q == "s" ? o == 2 || o == 3 ? (y = y || b.getBBox(1), k.scale(n[1], n[o - 1], y.x + y.width / 2, y.y + y.height / 2), h *= n[1], i *= n[o - 1]) : o == 5 && (s ? (w = t.x(n[3], n[4]), x = t.y(n[3], n[4]), k.scale(n[1], n[2], w, x)) : k.scale(n[1], n[2], n[3], n[4]), h *= n[1], i *= n[2]) : q == "m" && o == 7 && k.add(n[1], n[2], n[3], n[4], n[5], n[6]), j.dirtyT = 1, b.matrix = k
        }
        b.matrix = k, j.sx = h, j.sy = i, j.deg = e, j.dx = f = k.e, j.dy = g = k.f, h == 1 && i == 1 && !e && j.bbox ? (j.bbox.x += +f, j.bbox.y += +g) : j.dirtyT = 1
    }, bO = function (a) {
        var b = a[0];
        switch (b.toLowerCase()) {
            case"t":
                return [b, 0, 0];
            case"m":
                return [b, 1, 0, 0, 1, 0, 0];
            case"r":
                return a.length == 4 ? [b, 0, a[2], a[3]] : [b, 0];
            case"s":
                return a.length == 5 ? [b, 1, 1, a[3], a[4]] : a.length == 3 ? [b, 1, 1] : [b, 1]
        }
    }, bP = a._equaliseTransform = function (b, c) {
        c = r(c).replace(/\.{3}|\u2026/g, b), b = a.parseTransformString(b) || [], c = a.parseTransformString(c) || [];
        var d = x(b.length, c.length), e = [], f = [], g = 0, h, i, j, k;
        for (; g < d; g++) {
            j = b[g] || bO(c[g]), k = c[g] || bO(j);
            if (j[0] != k[0] || j[0].toLowerCase() == "r" && (j[2] != k[2] || j[3] != k[3]) || j[0].toLowerCase() == "s" && (j[3] != k[3] || j[4] != k[4]))return;
            e[g] = [], f[g] = [];
            for (h = 0, i = x(j.length, k.length); h < i; h++)h in j && (e[g][h] = j[h]), h in k && (f[g][h] = k[h])
        }
        return {from: e, to: f}
    };
    a._getContainer = function (b, c, d, e) {
        var f;
        f = e == null && !a.is(b, "object") ? h.doc.getElementById(b) : b;
        if (f != null) {
            if (f.tagName)return c == null ? {
                container: f,
                width: f.style.pixelWidth || f.offsetWidth,
                height: f.style.pixelHeight || f.offsetHeight
            } : {container: f, width: c, height: d};
            return {container: 1, x: b, y: c, width: d, height: e}
        }
    }, a.pathToRelative = bz, a._engine = {}, a.path2curve = bG, a.matrix = function (a, b, c, d, e, f) {
        return new bQ(a, b, c, d, e, f)
    }, function (b) {
        function d(a) {
            var b = w.sqrt(c(a));
            a[0] && (a[0] /= b), a[1] && (a[1] /= b)
        }

        function c(a) {
            return a[0] * a[0] + a[1] * a[1]
        }

        b.add = function (a, b, c, d, e, f) {
            var g = [[], [], []], h = [[this.a, this.c, this.e], [this.b, this.d, this.f], [0, 0, 1]], i = [[a, c, e], [b, d, f], [0, 0, 1]], j, k, l, m;
            a && a instanceof bQ && (i = [[a.a, a.c, a.e], [a.b, a.d, a.f], [0, 0, 1]]);
            for (j = 0; j < 3; j++)for (k = 0; k < 3; k++) {
                m = 0;
                for (l = 0; l < 3; l++)m += h[j][l] * i[l][k];
                g[j][k] = m
            }
            this.a = g[0][0], this.b = g[1][0], this.c = g[0][1], this.d = g[1][1], this.e = g[0][2], this.f = g[1][2]
        }, b.invert = function () {
            var a = this, b = a.a * a.d - a.b * a.c;
            return new bQ(a.d / b, -a.b / b, -a.c / b, a.a / b, (a.c * a.f - a.d * a.e) / b, (a.b * a.e - a.a * a.f) / b)
        }, b.clone = function () {
            return new bQ(this.a, this.b, this.c, this.d, this.e, this.f)
        }, b.translate = function (a, b) {
            this.add(1, 0, 0, 1, a, b)
        }, b.scale = function (a, b, c, d) {
            b == null && (b = a), (c || d) && this.add(1, 0, 0, 1, c, d), this.add(a, 0, 0, b, 0, 0), (c || d) && this.add(1, 0, 0, 1, -c, -d)
        }, b.rotate = function (b, c, d) {
            b = a.rad(b), c = c || 0, d = d || 0;
            var e = +w.cos(b).toFixed(9), f = +w.sin(b).toFixed(9);
            this.add(e, f, -f, e, c, d), this.add(1, 0, 0, 1, -c, -d)
        }, b.x = function (a, b) {
            return a * this.a + b * this.c + this.e
        }, b.y = function (a, b) {
            return a * this.b + b * this.d + this.f
        }, b.get = function (a) {
            return +this[r.fromCharCode(97 + a)].toFixed(4)
        }, b.toString = function () {
            return a.svg ? "matrix(" + [this.get(0), this.get(1), this.get(2), this.get(3), this.get(4), this.get(5)].join() + ")" : [this.get(0), this.get(2), this.get(1), this.get(3), 0, 0].join()
        }, b.toFilter = function () {
            return "progid:DXImageTransform.Microsoft.Matrix(M11=" + this.get(0) + ", M12=" + this.get(2) + ", M21=" + this.get(1) + ", M22=" + this.get(3) + ", Dx=" + this.get(4) + ", Dy=" + this.get(5) + ", sizingmethod='auto expand')"
        }, b.offset = function () {
            return [this.e.toFixed(4), this.f.toFixed(4)]
        }, b.split = function () {
            var b = {};
            b.dx = this.e, b.dy = this.f;
            var e = [[this.a, this.c], [this.b, this.d]];
            b.scalex = w.sqrt(c(e[0])), d(e[0]), b.shear = e[0][0] * e[1][0] + e[0][1] * e[1][1], e[1] = [e[1][0] - e[0][0] * b.shear, e[1][1] - e[0][1] * b.shear], b.scaley = w.sqrt(c(e[1])), d(e[1]), b.shear /= b.scaley;
            var f = -e[0][1], g = e[1][1];
            g < 0 ? (b.rotate = a.deg(w.acos(g)), f < 0 && (b.rotate = 360 - b.rotate)) : b.rotate = a.deg(w.asin(f)), b.isSimple = !+b.shear.toFixed(9) && (b.scalex.toFixed(9) == b.scaley.toFixed(9) || !b.rotate), b.isSuperSimple = !+b.shear.toFixed(9) && b.scalex.toFixed(9) == b.scaley.toFixed(9) && !b.rotate, b.noRotation = !+b.shear.toFixed(9) && !b.rotate;
            return b
        }, b.toTransformString = function (a) {
            var b = a || this[s]();
            if (b.isSimple) {
                b.scalex = +b.scalex.toFixed(4), b.scaley = +b.scaley.toFixed(4), b.rotate = +b.rotate.toFixed(4);
                return (b.dx && b.dy ? "t" + [b.dx, b.dy] : p) + (b.scalex != 1 || b.scaley != 1 ? "s" + [b.scalex, b.scaley, 0, 0] : p) + (b.rotate ? "r" + [b.rotate, 0, 0] : p)
            }
            return "m" + [this.get(0), this.get(1), this.get(2), this.get(3), this.get(4), this.get(5)]
        }
    }(bQ.prototype);
    var bR = navigator.userAgent.match(/Version\/(.*?)\s/) || navigator.userAgent.match(/Chrome\/(\d+)/);
    navigator.vendor == "Apple Computer, Inc." && (bR && bR[1] < 4 || navigator.platform.slice(0, 2) == "iP") || navigator.vendor == "Google Inc." && bR && bR[1] < 8 ? k.safari = function () {
        var a = this.rect(-99, -99, this.width + 99, this.height + 99).attr({stroke: "none"});
        setTimeout(function () {
            a.remove()
        })
    } : k.safari = bd;
    var bS = function () {
        this.returnValue = !1
    }, bT = function () {
        return this.originalEvent.preventDefault()
    }, bU = function () {
        this.cancelBubble = !0
    }, bV = function () {
        return this.originalEvent.stopPropagation()
    }, bW = function () {
        if (h.doc.addEventListener)return function (a, b, c, d) {
            var e = o && u[b] ? u[b] : b, f = function (e) {
                var f = h.doc.documentElement.scrollTop || h.doc.body.scrollTop, i = h.doc.documentElement.scrollLeft || h.doc.body.scrollLeft, j = e.clientX + i, k = e.clientY + f;
                if (o && u[g](b))for (var l = 0, m = e.targetTouches && e.targetTouches.length; l < m; l++)if (e.targetTouches[l].target == a) {
                    var n = e;
                    e = e.targetTouches[l], e.originalEvent = n, e.preventDefault = bT, e.stopPropagation = bV;
                    break
                }
                return c.call(d, e, j, k)
            };
            a.addEventListener(e, f, !1);
            return function () {
                a.removeEventListener(e, f, !1);
                return !0
            }
        };
        if (h.doc.attachEvent)return function (a, b, c, d) {
            var e = function (a) {
                a = a || h.win.event;
                var b = h.doc.documentElement.scrollTop || h.doc.body.scrollTop, e = h.doc.documentElement.scrollLeft || h.doc.body.scrollLeft, f = a.clientX + e, g = a.clientY + b;
                a.preventDefault = a.preventDefault || bS, a.stopPropagation = a.stopPropagation || bU;
                return c.call(d, a, f, g)
            };
            a.attachEvent("on" + b, e);
            var f = function () {
                a.detachEvent("on" + b, e);
                return !0
            };
            return f
        }
    }(), bX = [], bY = function (a) {
        var b = a.clientX, c = a.clientY, d = h.doc.documentElement.scrollTop || h.doc.body.scrollTop, e = h.doc.documentElement.scrollLeft || h.doc.body.scrollLeft, f, g = bX.length;
        while (g--) {
            f = bX[g];
            if (o) {
                var i = a.touches.length, j;
                while (i--) {
                    j = a.touches[i];
                    if (j.identifier == f.el._drag.id) {
                        b = j.clientX, c = j.clientY, (a.originalEvent ? a.originalEvent : a).preventDefault();
                        break
                    }
                }
            } else a.preventDefault();
            var k = f.el.node, l, m = k.nextSibling, n = k.parentNode, p = k.style.display;
            h.win.opera && n.removeChild(k), k.style.display = "none", l = f.el.paper.getElementByPoint(b, c), k.style.display = p, h.win.opera && (m ? n.insertBefore(k, m) : n.appendChild(k)), l && eve("drag.over." + f.el.id, f.el, l), b += e, c += d, eve("drag.move." + f.el.id, f.move_scope || f.el, b - f.el._drag.x, c - f.el._drag.y, b, c, a)
        }
    }, bZ = function (b) {
        a.unmousemove(bY).unmouseup(bZ);
        var c = bX.length, d;
        while (c--)d = bX[c], d.el._drag = {}, eve("drag.end." + d.el.id, d.end_scope || d.start_scope || d.move_scope || d.el, b);
        bX = []
    }, b$ = a.el = {};
    for (var b_ = t.length; b_--;)(function (b) {
        a[b] = b$[b] = function (c, d) {
            a.is(c, "function") && (this.events = this.events || [], this.events.push({
                name: b,
                f: c,
                unbind: bW(this.shape || this.node || h.doc, b, c, d || this)
            }));
            return this
        }, a["un" + b] = b$["un" + b] = function (a) {
            var c = this.events, d = c.length;
            while (d--)if (c[d].name == b && c[d].f == a) {
                c[d].unbind(), c.splice(d, 1), !c.length && delete this.events;
                return this
            }
            return this
        }
    })(t[b_]);
    b$.data = function (b, c) {
        var d = ba[this.id] = ba[this.id] || {};
        if (arguments.length == 1) {
            if (a.is(b, "object")) {
                for (var e in b)b[g](e) && this.data(e, b[e]);
                return this
            }
            eve("data.get." + this.id, this, d[b], b);
            return d[b]
        }
        d[b] = c, eve("data.set." + this.id, this, c, b);
        return this
    }, b$.removeData = function (a) {
        a == null ? ba[this.id] = {} : ba[this.id] && delete ba[this.id][a];
        return this
    }, b$.hover = function (a, b, c, d) {
        return this.mouseover(a, c).mouseout(b, d || c)
    }, b$.unhover = function (a, b) {
        return this.unmouseover(a).unmouseout(b)
    };
    var ca = [];
    b$.drag = function (b, c, d, e, f, g) {
        function i(i) {
            (i.originalEvent || i).preventDefault();
            var j = h.doc.documentElement.scrollTop || h.doc.body.scrollTop, k = h.doc.documentElement.scrollLeft || h.doc.body.scrollLeft;
            this._drag.x = i.clientX + k, this._drag.y = i.clientY + j, this._drag.id = i.identifier, !bX.length && a.mousemove(bY).mouseup(bZ), bX.push({
                el: this,
                move_scope: e,
                start_scope: f,
                end_scope: g
            }), c && eve.on("drag.start." + this.id, c), b && eve.on("drag.move." + this.id, b), d && eve.on("drag.end." + this.id, d), eve("drag.start." + this.id, f || e || this, i.clientX + k, i.clientY + j, i)
        }

        this._drag = {}, ca.push({el: this, start: i}), this.mousedown(i);
        return this
    }, b$.onDragOver = function (a) {
        a ? eve.on("drag.over." + this.id, a) : eve.unbind("drag.over." + this.id)
    }, b$.undrag = function () {
        var b = ca.length;
        while (b--)ca[b].el == this && (this.unmousedown(ca[b].start), ca.splice(b, 1), eve.unbind("drag.*." + this.id));
        !ca.length && a.unmousemove(bY).unmouseup(bZ)
    }, k.circle = function (b, c, d) {
        var e = a._engine.circle(this, b || 0, c || 0, d || 0);
        this.__set__ && this.__set__.push(e);
        return e
    }, k.rect = function (b, c, d, e, f) {
        var g = a._engine.rect(this, b || 0, c || 0, d || 0, e || 0, f || 0);
        this.__set__ && this.__set__.push(g);
        return g
    }, k.ellipse = function (b, c, d, e) {
        var f = a._engine.ellipse(this, b || 0, c || 0, d || 0, e || 0);
        this.__set__ && this.__set__.push(f);
        return f
    }, k.path = function (b) {
        b && !a.is(b, D) && !a.is(b[0], E) && (b += p);
        var c = a._engine.path(a.format[m](a, arguments), this);
        this.__set__ && this.__set__.push(c);
        return c
    }, k.image = function (b, c, d, e, f) {
        var g = a._engine.image(this, b || "about:blank", c || 0, d || 0, e || 0, f || 0);
        this.__set__ && this.__set__.push(g);
        return g
    }, k.text = function (b, c, d) {
        var e = a._engine.text(this, b || 0, c || 0, r(d));
        this.__set__ && this.__set__.push(e);
        return e
    }, k.set = function (b) {
        !a.is(b, "array") && (b = Array.prototype.splice.call(arguments, 0, arguments.length));
        var c = new cs(b);
        this.__set__ && this.__set__.push(c);
        return c
    }, k.setStart = function (a) {
        this.__set__ = a || this.set()
    }, k.setFinish = function (a) {
        var b = this.__set__;
        delete this.__set__;
        return b
    }, k.setSize = function (b, c) {
        return a._engine.setSize.call(this, b, c)
    }, k.setViewBox = function (b, c, d, e, f) {
        return a._engine.setViewBox.call(this, b, c, d, e, f)
    }, k.top = k.bottom = null, k.raphael = a;
    var cb = function (a) {
        var b = a.getBoundingClientRect(), c = a.ownerDocument, d = c.body, e = c.documentElement, f = e.clientTop || d.clientTop || 0, g = e.clientLeft || d.clientLeft || 0, i = b.top + (h.win.pageYOffset || e.scrollTop || d.scrollTop) - f, j = b.left + (h.win.pageXOffset || e.scrollLeft || d.scrollLeft) - g;
        return {y: i, x: j}
    };
    k.getElementByPoint = function (a, b) {
        var c = this, d = c.canvas, e = h.doc.elementFromPoint(a, b);
        if (h.win.opera && e.tagName == "svg") {
            var f = cb(d), g = d.createSVGRect();
            g.x = a - f.x, g.y = b - f.y, g.width = g.height = 1;
            var i = d.getIntersectionList(g, null);
            i.length && (e = i[i.length - 1])
        }
        if (!e)return null;
        while (e.parentNode && e != d.parentNode && !e.raphael)e = e.parentNode;
        e == c.canvas.parentNode && (e = d), e = e && e.raphael ? c.getById(e.raphaelid) : null;
        return e
    }, k.getById = function (a) {
        var b = this.bottom;
        while (b) {
            if (b.id == a)return b;
            b = b.next
        }
        return null
    }, k.forEach = function (a, b) {
        var c = this.bottom;
        while (c) {
            if (a.call(b, c) === !1)return this;
            c = c.next
        }
        return this
    }, b$.getBBox = function (a) {
        if (this.removed)return {};
        var b = this._;
        if (a) {
            if (b.dirty || !b.bboxwt)this.realPath = bh[this.type](this), b.bboxwt = bx(this.realPath), b.bboxwt.toString = cd, b.dirty = 0;
            return b.bboxwt
        }
        if (b.dirty || b.dirtyT || !b.bbox) {
            if (b.dirty || !this.realPath)b.bboxwt = 0, this.realPath = bh[this.type](this);
            b.bbox = bx(bi(this.realPath, this.matrix)), b.bbox.toString = cd, b.dirty = b.dirtyT = 0
        }
        return b.bbox
    }, b$.clone = function () {
        if (this.removed)return null;
        var a = this.paper[this.type]().attr(this.attr());
        this.__set__ && this.__set__.push(a);
        return a
    }, b$.glow = function (a) {
        if (this.type == "text")return null;
        a = a || {};
        var b = {
            width: (a.width || 10) + (+this.attr("stroke-width") || 1),
            fill: a.fill || !1,
            opacity: a.opacity || .5,
            offsetx: a.offsetx || 0,
            offsety: a.offsety || 0,
            color: a.color || "#000"
        }, c = b.width / 2, d = this.paper, e = d.set(), f = this.realPath || bh[this.type](this);
        f = this.matrix ? bi(f, this.matrix) : f;
        for (var g = 1; g < c + 1; g++)e.push(d.path(f).attr({
            stroke: b.color,
            fill: b.fill ? b.color : "none",
            "stroke-linejoin": "round",
            "stroke-linecap": "round",
            "stroke-width": +(b.width / c * g).toFixed(3),
            opacity: +(b.opacity / c).toFixed(3)
        }));
        return e.insertBefore(this).translate(b.offsetx, b.offsety)
    };
    var ce = {}, cf = function (b, c, d, e, f, g, h, i, j) {
        var k = 0, l = 100, m = [b, c, d, e, f, g, h, i].join(), n = ce[m], o, p;
        !n && (ce[m] = n = {data: []}), n.timer && clearTimeout(n.timer), n.timer = setTimeout(function () {
            delete ce[m]
        }, 2e3);
        if (j != null && !n.precision) {
            var q = cf(b, c, d, e, f, g, h, i);
            n.precision = ~~q * 10, n.data = []
        }
        l = n.precision || l;
        for (var r = 0; r < l + 1; r++) {
            n.data[r * l] ? p = n.data[r * l] : (p = a.findDotsAtSegment(b, c, d, e, f, g, h, i, r / l), n.data[r * l] = p), r && (k += A(A(o.x - p.x, 2) + A(o.y - p.y, 2), .5));
            if (j != null && k >= j)return p;
            o = p
        }
        if (j == null)return k
    }, cg = function (b, c) {
        return function (d, e, f) {
            d = bG(d);
            var g, h, i, j, k = "", l = {}, m, n = 0;
            for (var o = 0, p = d.length; o < p; o++) {
                i = d[o];
                if (i[0] == "M")g = +i[1], h = +i[2]; else {
                    j = cf(g, h, i[1], i[2], i[3], i[4], i[5], i[6]);
                    if (n + j > e) {
                        if (c && !l.start) {
                            m = cf(g, h, i[1], i[2], i[3], i[4], i[5], i[6], e - n), k += ["C" + m.start.x, m.start.y, m.m.x, m.m.y, m.x, m.y];
                            if (f)return k;
                            l.start = k, k = ["M" + m.x, m.y + "C" + m.n.x, m.n.y, m.end.x, m.end.y, i[5], i[6]].join(), n += j, g = +i[5], h = +i[6];
                            continue
                        }
                        if (!b && !c) {
                            m = cf(g, h, i[1], i[2], i[3], i[4], i[5], i[6], e - n);
                            return {x: m.x, y: m.y, alpha: m.alpha}
                        }
                    }
                    n += j, g = +i[5], h = +i[6]
                }
                k += i.shift() + i
            }
            l.end = k, m = b ? n : c ? l : a.findDotsAtSegment(g, h, i[0], i[1], i[2], i[3], i[4], i[5], 1), m.alpha && (m = {
                x: m.x,
                y: m.y,
                alpha: m.alpha
            });
            return m
        }
    }, ch = cg(1), ci = cg(), cj = cg(0, 1);
    a.getTotalLength = ch, a.getPointAtLength = ci, a.getSubpath = function (a, b, c) {
        if (this.getTotalLength(a) - c < 1e-6)return cj(a, b).end;
        var d = cj(a, c, 1);
        return b ? cj(d, b).end : d
    }, b$.getTotalLength = function () {
        if (this.type == "path") {
            if (this.node.getTotalLength)return this.node.getTotalLength();
            return ch(this.attrs.path)
        }
    }, b$.getPointAtLength = function (a) {
        if (this.type == "path")return ci(this.attrs.path, a)
    }, b$.getSubpath = function (b, c) {
        if (this.type == "path")return a.getSubpath(this.attrs.path, b, c)
    };
    var ck = a.easing_formulas = {
        linear: function (a) {
            return a
        }, "<": function (a) {
            return A(a, 1.7)
        }, ">": function (a) {
            return A(a, .48)
        }, "<>": function (a) {
            var b = .48 - a / 1.04, c = w.sqrt(.1734 + b * b), d = c - b, e = A(z(d), 1 / 3) * (d < 0 ? -1 : 1), f = -c - b, g = A(z(f), 1 / 3) * (f < 0 ? -1 : 1), h = e + g + .5;
            return (1 - h) * 3 * h * h + h * h * h
        }, backIn: function (a) {
            var b = 1.70158;
            return a * a * ((b + 1) * a - b)
        }, backOut: function (a) {
            a = a - 1;
            var b = 1.70158;
            return a * a * ((b + 1) * a + b) + 1
        }, elastic: function (a) {
            if (a == !!a)return a;
            return A(2, -10 * a) * w.sin((a - .075) * 2 * B / .3) + 1
        }, bounce: function (a) {
            var b = 7.5625, c = 2.75, d;
            a < 1 / c ? d = b * a * a : a < 2 / c ? (a -= 1.5 / c, d = b * a * a + .75) : a < 2.5 / c ? (a -= 2.25 / c, d = b * a * a + .9375) : (a -= 2.625 / c, d = b * a * a + .984375);
            return d
        }
    };
    ck.easeIn = ck["ease-in"] = ck["<"], ck.easeOut = ck["ease-out"] = ck[">"], ck.easeInOut = ck["ease-in-out"] = ck["<>"], ck["back-in"] = ck.backIn, ck["back-out"] = ck.backOut;
    var cl = [], cm = window.requestAnimationFrame || window.webkitRequestAnimationFrame || window.mozRequestAnimationFrame || window.oRequestAnimationFrame || window.msRequestAnimationFrame || function (a) {
            setTimeout(a, 16)
        }, cn = function () {
        var b = +(new Date), c = 0;
        for (; c < cl.length; c++) {
            var d = cl[c];
            if (d.el.removed || d.paused)continue;
            var e = b - d.start, f = d.ms, h = d.easing, i = d.from, j = d.diff, k = d.to, l = d.t, m = d.el, o = {}, p, r = {}, s;
            d.initstatus ? (e = (d.initstatus * d.anim.top - d.prev) / (d.percent - d.prev) * f, d.status = d.initstatus, delete d.initstatus, d.stop && cl.splice(c--, 1)) : d.status = (d.prev + (d.percent - d.prev) * (e / f)) / d.anim.top;
            if (e < 0)continue;
            if (e < f) {
                var t = h(e / f);
                for (var u in i)if (i[g](u)) {
                    switch (U[u]) {
                        case C:
                            p = +i[u] + t * f * j[u];
                            break;
                        case"colour":
                            p = "rgb(" + [co(O(i[u].r + t * f * j[u].r)), co(O(i[u].g + t * f * j[u].g)), co(O(i[u].b + t * f * j[u].b))].join(",") + ")";
                            break;
                        case"path":
                            p = [];
                            for (var v = 0, w = i[u].length; v < w; v++) {
                                p[v] = [i[u][v][0]];
                                for (var x = 1, y = i[u][v].length; x < y; x++)p[v][x] = +i[u][v][x] + t * f * j[u][v][x];
                                p[v] = p[v].join(q)
                            }
                            p = p.join(q);
                            break;
                        case"transform":
                            if (j[u].real) {
                                p = [];
                                for (v = 0, w = i[u].length; v < w; v++) {
                                    p[v] = [i[u][v][0]];
                                    for (x = 1, y = i[u][v].length; x < y; x++)p[v][x] = i[u][v][x] + t * f * j[u][v][x]
                                }
                            } else {
                                var z = function (a) {
                                    return +i[u][a] + t * f * j[u][a]
                                };
                                p = [["m", z(0), z(1), z(2), z(3), z(4), z(5)]]
                            }
                            break;
                        case"csv":
                            if (u == "clip-rect") {
                                p = [], v = 4;
                                while (v--)p[v] = +i[u][v] + t * f * j[u][v]
                            }
                            break;
                        default:
                            var A = [][n](i[u]);
                            p = [], v = m.paper.customAttributes[u].length;
                            while (v--)p[v] = +A[v] + t * f * j[u][v]
                    }
                    o[u] = p
                }
                m.attr(o), function (a, b, c) {
                    setTimeout(function () {
                        eve("anim.frame." + a, b, c)
                    })
                }(m.id, m, d.anim)
            } else {
                (function (b, c, d) {
                    setTimeout(function () {
                        eve("anim.frame." + c.id, c, d), eve("anim.finish." + c.id, c, d), a.is(b, "function") && b.call(c)
                    })
                })(d.callback, m, d.anim), m.attr(k), cl.splice(c--, 1);
                if (d.repeat > 1 && !d.next) {
                    for (s in k)k[g](s) && (r[s] = d.totalOrigin[s]);
                    d.el.attr(r), cr(d.anim, d.el, d.anim.percents[0], null, d.totalOrigin, d.repeat - 1)
                }
                d.next && !d.stop && cr(d.anim, d.el, d.next, null, d.totalOrigin, d.repeat)
            }
        }
        a.svg && m && m.paper && m.paper.safari(), cl.length && cm(cn)
    }, co = function (a) {
        return a > 255 ? 255 : a < 0 ? 0 : a
    };
    b$.animateWith = function (b, c, d, e, f, g) {
        var h = d ? a.animation(d, e, f, g) : c, i = b.status(c);
        return this.animate(h).status(h, i * c.ms / h.ms)
    }, b$.onAnimation = function (a) {
        a ? eve.on("anim.frame." + this.id, a) : eve.unbind("anim.frame." + this.id);
        return this
    }, cq.prototype.delay = function (a) {
        var b = new cq(this.anim, this.ms);
        b.times = this.times, b.del = +a || 0;
        return b
    }, cq.prototype.repeat = function (a) {
        var b = new cq(this.anim, this.ms);
        b.del = this.del, b.times = w.floor(x(a, 0)) || 1;
        return b
    }, a.animation = function (b, c, d, e) {
        if (b instanceof cq)return b;
        if (a.is(d, "function") || !d)e = e || d || null, d = null;
        b = Object(b), c = +c || 0;
        var f = {}, h, i;
        for (i in b)b[g](i) && Q(i) != i && Q(i) + "%" != i && (h = !0, f[i] = b[i]);
        if (!h)return new cq(b, c);
        d && (f.easing = d), e && (f.callback = e);
        return new cq({100: f}, c)
    }, b$.animate = function (b, c, d, e) {
        var f = this;
        if (f.removed) {
            e && e.call(f);
            return f
        }
        var g = b instanceof cq ? b : a.animation(b, c, d, e);
        cr(g, f, g.percents[0], null, f.attr());
        return f
    }, b$.setTime = function (a, b) {
        a && b != null && this.status(a, y(b, a.ms) / a.ms);
        return this
    }, b$.status = function (a, b) {
        var c = [], d = 0, e, f;
        if (b != null) {
            cr(a, this, -1, y(b, 1));
            return this
        }
        e = cl.length;
        for (; d < e; d++) {
            f = cl[d];
            if (f.el.id == this.id && (!a || f.anim == a)) {
                if (a)return f.status;
                c.push({anim: f.anim, status: f.status})
            }
        }
        if (a)return 0;
        return c
    }, b$.pause = function (a) {
        for (var b = 0; b < cl.length; b++)cl[b].el.id == this.id && (!a || cl[b].anim == a) && eve("anim.pause." + this.id, this, cl[b].anim) !== !1 && (cl[b].paused = !0);
        return this
    }, b$.resume = function (a) {
        for (var b = 0; b < cl.length; b++)if (cl[b].el.id == this.id && (!a || cl[b].anim == a)) {
            var c = cl[b];
            eve("anim.resume." + this.id, this, c.anim) !== !1 && (delete c.paused, this.status(c.anim, c.status))
        }
        return this
    }, b$.stop = function (a) {
        for (var b = 0; b < cl.length; b++)cl[b].el.id == this.id && (!a || cl[b].anim == a) && eve("anim.stop." + this.id, this, cl[b].anim) !== !1 && cl.splice(b--, 1);
        return this
    }, b$.toString = function () {
        return "Raphaël’s object"
    };
    var cs = function (a) {
        this.items = [], this.length = 0, this.type = "set";
        if (a)for (var b = 0, c = a.length; b < c; b++)a[b] && (a[b].constructor == b$.constructor || a[b].constructor == cs) && (this[this.items.length] = this.items[this.items.length] = a[b], this.length++)
    }, ct = cs.prototype;
    ct.push = function () {
        var a, b;
        for (var c = 0, d = arguments.length; c < d; c++)a = arguments[c], a && (a.constructor == b$.constructor || a.constructor == cs) && (b = this.items.length, this[b] = this.items[b] = a, this.length++);
        return this
    }, ct.pop = function () {
        this.length && delete this[this.length--];
        return this.items.pop()
    }, ct.forEach = function (a, b) {
        for (var c = 0, d = this.items.length; c < d; c++)if (a.call(b, this.items[c], c) === !1)return this;
        return this
    };
    for (var cu in b$)b$[g](cu) && (ct[cu] = function (a) {
        return function () {
            var b = arguments;
            return this.forEach(function (c) {
                c[a][m](c, b)
            })
        }
    }(cu));
    ct.attr = function (b, c) {
        if (b && a.is(b, E) && a.is(b[0], "object"))for (var d = 0, e = b.length; d < e; d++)this.items[d].attr(b[d]); else for (var f = 0, g = this.items.length; f < g; f++)this.items[f].attr(b, c);
        return this
    }, ct.clear = function () {
        while (this.length)this.pop()
    }, ct.splice = function (a, b, c) {
        a = a < 0 ? x(this.length + a, 0) : a, b = x(0, y(this.length - a, b));
        var d = [], e = [], f = [], g;
        for (g = 2; g < arguments.length; g++)f.push(arguments[g]);
        for (g = 0; g < b; g++)e.push(this[a + g]);
        for (; g < this.length - a; g++)d.push(this[a + g]);
        var h = f.length;
        for (g = 0; g < h + d.length; g++)this.items[a + g] = this[a + g] = g < h ? f[g] : d[g - h];
        g = this.items.length = this.length -= b - h;
        while (this[g])delete this[g++];
        return new cs(e)
    }, ct.exclude = function (a) {
        for (var b = 0, c = this.length; b < c; b++)if (this[b] == a) {
            this.splice(b, 1);
            return !0
        }
    }, ct.animate = function (b, c, d, e) {
        (a.is(d, "function") || !d) && (e = d || null);
        var f = this.items.length, g = f, h, i = this, j;
        if (!f)return this;
        e && (j = function () {
            !--f && e.call(i)
        }), d = a.is(d, D) ? d : j;
        var k = a.animation(b, c, d, j);
        h = this.items[--g].animate(k);
        while (g--)this.items[g] && !this.items[g].removed && this.items[g].animateWith(h, k);
        return this
    }, ct.insertAfter = function (a) {
        var b = this.items.length;
        while (b--)this.items[b].insertAfter(a);
        return this
    }, ct.getBBox = function () {
        var a = [], b = [], c = [], d = [];
        for (var e = this.items.length; e--;)if (!this.items[e].removed) {
            var f = this.items[e].getBBox();
            a.push(f.x), b.push(f.y), c.push(f.x + f.width), d.push(f.y + f.height)
        }
        a = y[m](0, a), b = y[m](0, b);
        return {x: a, y: b, width: x[m](0, c) - a, height: x[m](0, d) - b}
    }, ct.clone = function (a) {
        a = new cs;
        for (var b = 0, c = this.items.length; b < c; b++)a.push(this.items[b].clone());
        return a
    }, ct.toString = function () {
        return "Raphaël‘s set"
    }, a.registerFont = function (a) {
        if (!a.face)return a;
        this.fonts = this.fonts || {};
        var b = {w: a.w, face: {}, glyphs: {}}, c = a.face["font-family"];
        for (var d in a.face)a.face[g](d) && (b.face[d] = a.face[d]);
        this.fonts[c] ? this.fonts[c].push(b) : this.fonts[c] = [b];
        if (!a.svg) {
            b.face["units-per-em"] = R(a.face["units-per-em"], 10);
            for (var e in a.glyphs)if (a.glyphs[g](e)) {
                var f = a.glyphs[e];
                b.glyphs[e] = {
                    w: f.w, k: {}, d: f.d && "M" + f.d.replace(/[mlcxtrv]/g, function (a) {
                        return {l: "L", c: "C", x: "z", t: "m", r: "l", v: "c"}[a] || "M"
                    }) + "z"
                };
                if (f.k)for (var h in f.k)f[g](h) && (b.glyphs[e].k[h] = f.k[h])
            }
        }
        return a
    }, k.getFont = function (b, c, d, e) {
        e = e || "normal", d = d || "normal", c = +c || {normal: 400, bold: 700, lighter: 300, bolder: 800}[c] || 400;
        if (!!a.fonts) {
            var f = a.fonts[b];
            if (!f) {
                var h = new RegExp("(^|\\s)" + b.replace(/[^\w\d\s+!~.:_-]/g, p) + "(\\s|$)", "i");
                for (var i in a.fonts)if (a.fonts[g](i) && h.test(i)) {
                    f = a.fonts[i];
                    break
                }
            }
            var j;
            if (f)for (var k = 0, l = f.length; k < l; k++) {
                j = f[k];
                if (j.face["font-weight"] == c && (j.face["font-style"] == d || !j.face["font-style"]) && j.face["font-stretch"] == e)break
            }
            return j
        }
    }, k.print = function (b, d, e, f, g, h, i) {
        h = h || "middle", i = x(y(i || 0, 1), -1);
        var j = this.set(), k = r(e)[s](p), l = 0, m = p, n;
        a.is(f, e) && (f = this.getFont(f));
        if (f) {
            n = (g || 16) / f.face["units-per-em"];
            var o = f.face.bbox[s](c), q = +o[0], t = +o[1] + (h == "baseline" ? o[3] - o[1] + +f.face.descent : (o[3] - o[1]) / 2);
            for (var u = 0, v = k.length; u < v; u++) {
                var w = u && f.glyphs[k[u - 1]] || {}, z = f.glyphs[k[u]];
                l += u ? (w.w || f.w) + (w.k && w.k[k[u]] || 0) + f.w * i : 0, z && z.d && j.push(this.path(z.d).attr({
                    fill: "#000",
                    stroke: "none",
                    transform: [["t", l * n, 0]]
                }))
            }
            j.transform(["...s", n, n, q, t, "t", (b - q) / n, (d - t) / n])
        }
        return j
    }, k.add = function (b) {
        if (a.is(b, "array")) {
            var c = this.set(), e = 0, f = b.length, h;
            for (; e < f; e++)h = b[e] || {}, d[g](h.type) && c.push(this[h.type]().attr(h))
        }
        return c
    }, a.format = function (b, c) {
        var d = a.is(c, E) ? [0][n](c) : arguments;
        b && a.is(b, D) && d.length - 1 && (b = b.replace(e, function (a, b) {
            return d[++b] == null ? p : d[b]
        }));
        return b || p
    }, a.fullfill = function () {
        var a = /\{([^\}]+)\}/g, b = /(?:(?:^|\.)(.+?)(?=\[|\.|$|\()|\[('|")(.+?)\2\])(\(\))?/g, c = function (a, c, d) {
            var e = d;
            c.replace(b, function (a, b, c, d, f) {
                b = b || d, e && (b in e && (e = e[b]), typeof e == "function" && f && (e = e()))
            }), e = (e == null || e == d ? a : e) + "";
            return e
        };
        return function (b, d) {
            return String(b).replace(a, function (a, b) {
                return c(a, b, d)
            })
        }
    }(), a.ninja = function () {
        i.was ? h.win.Raphael = i.is : delete Raphael;
        return a
    }, a.st = ct, function (b, c, d) {
        function e() {
            /in/.test(b.readyState) ? setTimeout(e, 9) : a.eve("DOMload")
        }

        b.readyState == null && b.addEventListener && (b.addEventListener(c, d = function () {
            b.removeEventListener(c, d, !1), b.readyState = "complete"
        }, !1), b.readyState = "loading"), e()
    }(document, "DOMContentLoaded"), i.was ? h.win.Raphael = a : Raphael = a, eve.on("DOMload", function () {
        b = !0
    })
}(), window.Raphael.svg && function (a) {
    var b = "hasOwnProperty", c = String, d = parseFloat, e = parseInt, f = Math, g = f.max, h = f.abs, i = f.pow, j = /[, ]+/, k = a.eve, l = "", m = " ", n = "http://www.w3.org/1999/xlink", o = {
        block: "M5,0 0,2.5 5,5z",
        classic: "M5,0 0,2.5 5,5 3.5,3 3.5,2z",
        diamond: "M2.5,0 5,2.5 2.5,5 0,2.5z",
        open: "M6,1 1,3.5 6,6",
        oval: "M2.5,0A2.5,2.5,0,0,1,2.5,5 2.5,2.5,0,0,1,2.5,0z"
    }, p = {};
    a.toString = function () {
        return "Your browser supports SVG.\nYou are running Raphaël " + this.version
    };
    var q = function (d, e) {
        if (e) {
            typeof d == "string" && (d = q(d));
            for (var f in e)e[b](f) && (f.substring(0, 6) == "xlink:" ? d.setAttributeNS(n, f.substring(6), c(e[f])) : d.setAttribute(f, c(e[f])))
        } else d = a._g.doc.createElementNS("http://www.w3.org/2000/svg", d), d.style && (d.style.webkitTapHighlightColor = "rgba(0,0,0,0)");
        return d
    }, r = function (b, e) {
        var j = "linear", k = b.id + e, m = .5, n = .5, o = b.node, p = b.paper, r = o.style, s = a._g.doc.getElementById(k);
        if (!s) {
            e = c(e).replace(a._radial_gradient, function (a, b, c) {
                j = "radial";
                if (b && c) {
                    m = d(b), n = d(c);
                    var e = (n > .5) * 2 - 1;
                    i(m - .5, 2) + i(n - .5, 2) > .25 && (n = f.sqrt(.25 - i(m - .5, 2)) * e + .5) && n != .5 && (n = n.toFixed(5) - 1e-5 * e)
                }
                return l
            }), e = e.split(/\s*\-\s*/);
            if (j == "linear") {
                var t = e.shift();
                t = -d(t);
                if (isNaN(t))return null;
                var u = [0, 0, f.cos(a.rad(t)), f.sin(a.rad(t))], v = 1 / (g(h(u[2]), h(u[3])) || 1);
                u[2] *= v, u[3] *= v, u[2] < 0 && (u[0] = -u[2], u[2] = 0), u[3] < 0 && (u[1] = -u[3], u[3] = 0)
            }
            var w = a._parseDots(e);
            if (!w)return null;
            k = k.replace(/[\(\)\s,\xb0#]/g, "_"), b.gradient && k != b.gradient.id && (p.defs.removeChild(b.gradient), delete b.gradient);
            if (!b.gradient) {
                s = q(j + "Gradient", {id: k}), b.gradient = s, q(s, j == "radial" ? {fx: m, fy: n} : {
                    x1: u[0],
                    y1: u[1],
                    x2: u[2],
                    y2: u[3],
                    gradientTransform: b.matrix.invert()
                }), p.defs.appendChild(s);
                for (var x = 0, y = w.length; x < y; x++)s.appendChild(q("stop", {
                    offset: w[x].offset ? w[x].offset : x ? "100%" : "0%",
                    "stop-color": w[x].color || "#fff"
                }))
            }
        }
        q(o, {fill: "url(#" + k + ")", opacity: 1, "fill-opacity": 1}), r.fill = l, r.opacity = 1, r.fillOpacity = 1;
        return 1
    }, s = function (a) {
        var b = a.getBBox(1);
        q(a.pattern, {patternTransform: a.matrix.invert() + " translate(" + b.x + "," + b.y + ")"})
    }, t = function (d, e, f) {
        if (d.type == "path") {
            var g = c(e).toLowerCase().split("-"), h = d.paper, i = f ? "end" : "start", j = d.node, k = d.attrs, l = k["stroke-width"], n = g.length, r = "classic", s, t, u, v, w, x = 3, y = 3, z = 5;
            while (n--)switch (g[n]) {
                case"block":
                case"classic":
                case"oval":
                case"diamond":
                case"open":
                case"none":
                    r = g[n];
                    break;
                case"wide":
                    y = 5;
                    break;
                case"narrow":
                    y = 2;
                    break;
                case"long":
                    x = 5;
                    break;
                case"short":
                    x = 2
            }
            r == "open" ? (x += 2, y += 2, z += 2, u = 1, v = f ? 4 : 1, w = {
                fill: "none",
                stroke: k.stroke
            }) : (v = u = x / 2, w = {
                fill: k.stroke,
                stroke: "none"
            }), d._.arrows ? f ? (d._.arrows.endPath && p[d._.arrows.endPath]--, d._.arrows.endMarker && p[d._.arrows.endMarker]--) : (d._.arrows.startPath && p[d._.arrows.startPath]--, d._.arrows.startMarker && p[d._.arrows.startMarker]--) : d._.arrows = {};
            if (r != "none") {
                var A = "raphael-marker-" + r, B = "raphael-marker-" + i + r + x + y;
                a._g.doc.getElementById(A) ? p[A]++ : (h.defs.appendChild(q(q("path"), {
                    "stroke-linecap": "round",
                    d: o[r],
                    id: A
                })), p[A] = 1);
                var C = a._g.doc.getElementById(B), D;
                C ? (p[B]++, D = C.getElementsByTagName("use")[0]) : (C = q(q("marker"), {
                    id: B,
                    markerHeight: y,
                    markerWidth: x,
                    orient: "auto",
                    refX: v,
                    refY: y / 2
                }), D = q(q("use"), {
                    "xlink:href": "#" + A,
                    transform: (f ? " rotate(180 " + x / 2 + " " + y / 2 + ") " : m) + "scale(" + x / z + "," + y / z + ")",
                    "stroke-width": 1 / ((x / z + y / z) / 2)
                }), C.appendChild(D), h.defs.appendChild(C), p[B] = 1), q(D, w);
                var E = u * (r != "diamond" && r != "oval");
                f ? (s = d._.arrows.startdx * l || 0, t = a.getTotalLength(k.path) - E * l) : (s = E * l, t = a.getTotalLength(k.path) - (d._.arrows.enddx * l || 0)), w = {}, w["marker-" + i] = "url(#" + B + ")";
                if (t || s)w.d = Raphael.getSubpath(k.path, s, t);
                q(j, w), d._.arrows[i + "Path"] = A, d._.arrows[i + "Marker"] = B, d._.arrows[i + "dx"] = E, d._.arrows[i + "Type"] = r, d._.arrows[i + "String"] = e
            } else f ? (s = d._.arrows.startdx * l || 0, t = a.getTotalLength(k.path) - s) : (s = 0, t = a.getTotalLength(k.path) - (d._.arrows.enddx * l || 0)), d._.arrows[i + "Path"] && q(j, {d: Raphael.getSubpath(k.path, s, t)}), delete d._.arrows[i + "Path"], delete d._.arrows[i + "Marker"], delete d._.arrows[i + "dx"], delete d._.arrows[i + "Type"], delete d._.arrows[i + "String"];
            for (w in p)if (p[b](w) && !p[w]) {
                var F = a._g.doc.getElementById(w);
                F && F.parentNode.removeChild(F)
            }
        }
    }, u = {
        "": [0],
        none: [0],
        "-": [3, 1],
        ".": [1, 1],
        "-.": [3, 1, 1, 1],
        "-..": [3, 1, 1, 1, 1, 1],
        ". ": [1, 3],
        "- ": [4, 3],
        "--": [8, 3],
        "- .": [4, 3, 1, 3],
        "--.": [8, 3, 1, 3],
        "--..": [8, 3, 1, 3, 1, 3]
    }, v = function (a, b, d) {
        b = u[c(b).toLowerCase()];
        if (b) {
            var e = a.attrs["stroke-width"] || "1", f = {
                    round: e,
                    square: e,
                    butt: 0
                }[a.attrs["stroke-linecap"] || d["stroke-linecap"]] || 0, g = [], h = b.length;
            while (h--)g[h] = b[h] * e + (h % 2 ? 1 : -1) * f;
            q(a.node, {"stroke-dasharray": g.join(",")})
        }
    }, w = function (d, f) {
        var i = d.node, k = d.attrs, m = i.style.visibility;
        i.style.visibility = "hidden";
        for (var o in f)if (f[b](o)) {
            if (!a._availableAttrs[b](o))continue;
            var p = f[o];
            k[o] = p;
            switch (o) {
                case"blur":
                    d.blur(p);
                    break;
                case"href":
                case"title":
                case"target":
                    var u = i.parentNode;
                    if (u.tagName.toLowerCase() != "a") {
                        var w = q("a");
                        u.insertBefore(w, i), w.appendChild(i), u = w
                    }
                    o == "target" && p == "blank" ? u.setAttributeNS(n, "show", "new") : u.setAttributeNS(n, o, p);
                    break;
                case"cursor":
                    i.style.cursor = p;
                    break;
                case"transform":
                    d.transform(p);
                    break;
                case"arrow-start":
                    t(d, p);
                    break;
                case"arrow-end":
                    t(d, p, 1);
                    break;
                case"clip-rect":
                    var x = c(p).split(j);
                    if (x.length == 4) {
                        d.clip && d.clip.parentNode.parentNode.removeChild(d.clip.parentNode);
                        var z = q("clipPath"), A = q("rect");
                        z.id = a.createUUID(), q(A, {
                            x: x[0],
                            y: x[1],
                            width: x[2],
                            height: x[3]
                        }), z.appendChild(A), d.paper.defs.appendChild(z), q(i, {"clip-path": "url(#" + z.id + ")"}), d.clip = A
                    }
                    if (!p) {
                        var B = i.getAttribute("clip-path");
                        if (B) {
                            var C = a._g.doc.getElementById(B.replace(/(^url\(#|\)$)/g, l));
                            C && C.parentNode.removeChild(C), q(i, {"clip-path": l}), delete d.clip
                        }
                    }
                    break;
                case"path":
                    d.type == "path" && (q(i, {d: p ? k.path = a._pathToAbsolute(p) : "M0,0"}), d._.dirty = 1, d._.arrows && ("startString"in d._.arrows && t(d, d._.arrows.startString), "endString"in d._.arrows && t(d, d._.arrows.endString, 1)));
                    break;
                case"width":
                    i.setAttribute(o, p), d._.dirty = 1;
                    if (k.fx)o = "x", p = k.x; else break;
                case"x":
                    k.fx && (p = -k.x - (k.width || 0));
                case"rx":
                    if (o == "rx" && d.type == "rect")break;
                case"cx":
                    i.setAttribute(o, p), d.pattern && s(d), d._.dirty = 1;
                    break;
                case"height":
                    i.setAttribute(o, p), d._.dirty = 1;
                    if (k.fy)o = "y", p = k.y; else break;
                case"y":
                    k.fy && (p = -k.y - (k.height || 0));
                case"ry":
                    if (o == "ry" && d.type == "rect")break;
                case"cy":
                    i.setAttribute(o, p), d.pattern && s(d), d._.dirty = 1;
                    break;
                case"r":
                    d.type == "rect" ? q(i, {rx: p, ry: p}) : i.setAttribute(o, p), d._.dirty = 1;
                    break;
                case"src":
                    d.type == "image" && i.setAttributeNS(n, "href", p);
                    break;
                case"stroke-width":
                    if (d._.sx != 1 || d._.sy != 1)p /= g(h(d._.sx), h(d._.sy)) || 1;
                    d.paper._vbSize && (p *= d.paper._vbSize), i.setAttribute(o, p), k["stroke-dasharray"] && v(d, k["stroke-dasharray"], f), d._.arrows && ("startString"in d._.arrows && t(d, d._.arrows.startString), "endString"in d._.arrows && t(d, d._.arrows.endString, 1));
                    break;
                case"stroke-dasharray":
                    v(d, p, f);
                    break;
                case"fill":
                    var D = c(p).match(a._ISURL);
                    if (D) {
                        z = q("pattern");
                        var F = q("image");
                        z.id = a.createUUID(), q(z, {
                            x: 0,
                            y: 0,
                            patternUnits: "userSpaceOnUse",
                            height: 1,
                            width: 1
                        }), q(F, {x: 0, y: 0, "xlink:href": D[1]}), z.appendChild(F), function (b) {
                            a._preload(D[1], function () {
                                var a = this.offsetWidth, c = this.offsetHeight;
                                q(b, {width: a, height: c}), q(F, {width: a, height: c}), d.paper.safari()
                            })
                        }(z), d.paper.defs.appendChild(z), i.style.fill = "url(#" + z.id + ")", q(i, {fill: "url(#" + z.id + ")"}), d.pattern = z, d.pattern && s(d);
                        break
                    }
                    var G = a.getRGB(p);
                    if (!G.error)delete f.gradient, delete k.gradient, !a.is(k.opacity, "undefined") && a.is(f.opacity, "undefined") && q(i, {opacity: k.opacity}), !a.is(k["fill-opacity"], "undefined") && a.is(f["fill-opacity"], "undefined") && q(i, {"fill-opacity": k["fill-opacity"]}); else if ((d.type == "circle" || d.type == "ellipse" || c(p).charAt() != "r") && r(d, p)) {
                        if ("opacity"in k || "fill-opacity"in k) {
                            var H = a._g.doc.getElementById(i.getAttribute("fill").replace(/^url\(#|\)$/g, l));
                            if (H) {
                                var I = H.getElementsByTagName("stop");
                                q(I[I.length - 1], {"stop-opacity": ("opacity"in k ? k.opacity : 1) * ("fill-opacity"in k ? k["fill-opacity"] : 1)})
                            }
                        }
                        k.gradient = p, k.fill = "none";
                        break
                    }
                    G[b]("opacity") && q(i, {"fill-opacity": G.opacity > 1 ? G.opacity / 100 : G.opacity});
                case"stroke":
                    G = a.getRGB(p), i.setAttribute(o, G.hex), o == "stroke" && G[b]("opacity") && q(i, {"stroke-opacity": G.opacity > 1 ? G.opacity / 100 : G.opacity}), o == "stroke" && d._.arrows && ("startString"in d._.arrows && t(d, d._.arrows.startString), "endString"in d._.arrows && t(d, d._.arrows.endString, 1));
                    break;
                case"gradient":
                    (d.type == "circle" || d.type == "ellipse" || c(p).charAt() != "r") && r(d, p);
                    break;
                case"opacity":
                    k.gradient && !k[b]("stroke-opacity") && q(i, {"stroke-opacity": p > 1 ? p / 100 : p});
                case"fill-opacity":
                    if (k.gradient) {
                        H = a._g.doc.getElementById(i.getAttribute("fill").replace(/^url\(#|\)$/g, l)), H && (I = H.getElementsByTagName("stop"), q(I[I.length - 1], {"stop-opacity": p}));
                        break
                    }
                    ;
                default:
                    o == "font-size" && (p = e(p, 10) + "px");
                    var J = o.replace(/(\-.)/g, function (a) {
                        return a.substring(1).toUpperCase()
                    });
                    i.style[J] = p, d._.dirty = 1, i.setAttribute(o, p)
            }
        }
        y(d, f), i.style.visibility = m
    }, x = 1.2, y = function (d, f) {
        if (d.type == "text" && !!(f[b]("text") || f[b]("font") || f[b]("font-size") || f[b]("x") || f[b]("y"))) {
            var g = d.attrs, h = d.node, i = h.firstChild ? e(a._g.doc.defaultView.getComputedStyle(h.firstChild, l).getPropertyValue("font-size"), 10) : 10;
            if (f[b]("text")) {
                g.text = f.text;
                while (h.firstChild)h.removeChild(h.firstChild);
                var j = c(f.text).split("\n"), k = [], m;
                for (var n = 0, o = j.length; n < o; n++)m = q("tspan"), n && q(m, {
                    dy: i * x,
                    x: g.x
                }), m.appendChild(a._g.doc.createTextNode(j[n])), h.appendChild(m), k[n] = m
            } else {
                k = h.getElementsByTagName("tspan");
                for (n = 0, o = k.length; n < o; n++)n ? q(k[n], {dy: i * x, x: g.x}) : q(k[0], {dy: 0})
            }
            q(h, {x: g.x, y: g.y}), d._.dirty = 1;
            var p = d._getBBox(), r = g.y - (p.y + p.height / 2);
            r && a.is(r, "finite") && q(k[0], {dy: r})
        }
    }, z = function (b, c) {
        var d = 0, e = 0;
        this[0] = this.node = b, b.raphael = !0, this.id = a._oid++, b.raphaelid = this.id, this.matrix = a.matrix(), this.realPath = null, this.paper = c, this.attrs = this.attrs || {}, this._ = {
            transform: [],
            sx: 1,
            sy: 1,
            deg: 0,
            dx: 0,
            dy: 0,
            dirty: 1
        }, !c.bottom && (c.bottom = this), this.prev = c.top, c.top && (c.top.next = this), c.top = this, this.next = null
    }, A = a.el;
    z.prototype = A, A.constructor = z, a._engine.path = function (a, b) {
        var c = q("path");
        b.canvas && b.canvas.appendChild(c);
        var d = new z(c, b);
        d.type = "path", w(d, {fill: "none", stroke: "#000", path: a});
        return d
    }, A.rotate = function (a, b, e) {
        if (this.removed)return this;
        a = c(a).split(j), a.length - 1 && (b = d(a[1]), e = d(a[2])), a = d(a[0]), e == null && (b = e);
        if (b == null || e == null) {
            var f = this.getBBox(1);
            b = f.x + f.width / 2, e = f.y + f.height / 2
        }
        this.transform(this._.transform.concat([["r", a, b, e]]));
        return this
    }, A.scale = function (a, b, e, f) {
        if (this.removed)return this;
        a = c(a).split(j), a.length - 1 && (b = d(a[1]), e = d(a[2]), f = d(a[3])), a = d(a[0]), b == null && (b = a), f == null && (e = f);
        if (e == null || f == null)var g = this.getBBox(1);
        e = e == null ? g.x + g.width / 2 : e, f = f == null ? g.y + g.height / 2 : f, this.transform(this._.transform.concat([["s", a, b, e, f]]));
        return this
    }, A.translate = function (a, b) {
        if (this.removed)return this;
        a = c(a).split(j), a.length - 1 && (b = d(a[1])), a = d(a[0]) || 0, b = +b || 0, this.transform(this._.transform.concat([["t", a, b]]));
        return this
    }, A.transform = function (c) {
        var d = this._;
        if (c == null)return d.transform;
        a._extractTransform(this, c), this.clip && q(this.clip, {transform: this.matrix.invert()}), this.pattern && s(this), this.node && q(this.node, {transform: this.matrix});
        if (d.sx != 1 || d.sy != 1) {
            var e = this.attrs[b]("stroke-width") ? this.attrs["stroke-width"] : 1;
            this.attr({"stroke-width": e})
        }
        return this
    }, A.hide = function () {
        !this.removed && this.paper.safari(this.node.style.display = "none");
        return this
    }, A.show = function () {
        !this.removed && this.paper.safari(this.node.style.display = "");
        return this
    }, A.remove = function () {
        if (!this.removed) {
            var b = this.paper;
            b.__set__ && b.__set__.exclude(this), k.unbind("*.*." + this.id), this.gradient && b.defs.removeChild(this.gradient), a._tear(this, b), this.node.parentNode.removeChild(this.node);
            for (var c in this)this[c] = typeof this[c] == "function" ? a._removedFactory(c) : null;
            this.removed = !0
        }
    }, A._getBBox = function () {
        if (this.node.style.display == "none") {
            this.show();
            var a = !0
        }
        var b = {};
        try {
            b = this.node.getBBox()
        } catch (c) {
        } finally {
            b = b || {}
        }
        a && this.hide();
        return b
    }, A.attr = function (c, d) {
        if (this.removed)return this;
        if (c == null) {
            var e = {};
            for (var f in this.attrs)this.attrs[b](f) && (e[f] = this.attrs[f]);
            e.gradient && e.fill == "none" && (e.fill = e.gradient) && delete e.gradient, e.transform = this._.transform;
            return e
        }
        if (d == null && a.is(c, "string")) {
            if (c == "fill" && this.attrs.fill == "none" && this.attrs.gradient)return this.attrs.gradient;
            if (c == "transform")return this._.transform;
            var g = c.split(j), h = {};
            for (var i = 0, l = g.length; i < l; i++)c = g[i], c in this.attrs ? h[c] = this.attrs[c] : a.is(this.paper.customAttributes[c], "function") ? h[c] = this.paper.customAttributes[c].def : h[c] = a._availableAttrs[c];
            return l - 1 ? h : h[g[0]]
        }
        if (d == null && a.is(c, "array")) {
            h = {};
            for (i = 0, l = c.length; i < l; i++)h[c[i]] = this.attr(c[i]);
            return h
        }
        if (d != null) {
            var m = {};
            m[c] = d
        } else c != null && a.is(c, "object") && (m = c);
        for (var n in m)k("attr." + n + "." + this.id, this, m[n]);
        for (n in this.paper.customAttributes)if (this.paper.customAttributes[b](n) && m[b](n) && a.is(this.paper.customAttributes[n], "function")) {
            var o = this.paper.customAttributes[n].apply(this, [].concat(m[n]));
            this.attrs[n] = m[n];
            for (var p in o)o[b](p) && (m[p] = o[p])
        }
        w(this, m);
        return this
    }, A.toFront = function () {
        if (this.removed)return this;
        this.node.parentNode.tagName.toLowerCase() == "a" ? this.node.parentNode.parentNode.appendChild(this.node.parentNode) : this.node.parentNode.appendChild(this.node);
        var b = this.paper;
        b.top != this && a._tofront(this, b);
        return this
    }, A.toBack = function () {
        if (this.removed)return this;
        var b = this.node.parentNode;
        b.tagName.toLowerCase() == "a" ? b.parentNode.insertBefore(this.node.parentNode, this.node.parentNode.parentNode.firstChild) : b.firstChild != this.node && b.insertBefore(this.node, this.node.parentNode.firstChild), a._toback(this, this.paper);
        var c = this.paper;
        return this
    }, A.insertAfter = function (b) {
        if (this.removed)return this;
        var c = b.node || b[b.length - 1].node;
        c.nextSibling ? c.parentNode.insertBefore(this.node, c.nextSibling) : c.parentNode.appendChild(this.node), a._insertafter(this, b, this.paper);
        return this
    }, A.insertBefore = function (b) {
        if (this.removed)return this;
        var c = b.node || b[0].node;
        c.parentNode.insertBefore(this.node, c), a._insertbefore(this, b, this.paper);
        return this
    }, A.blur = function (b) {
        var c = this;
        if (+b !== 0) {
            var d = q("filter"), e = q("feGaussianBlur");
            c.attrs.blur = b, d.id = a.createUUID(), q(e, {stdDeviation: +b || 1.5}), d.appendChild(e), c.paper.defs.appendChild(d), c._blur = d, q(c.node, {filter: "url(#" + d.id + ")"})
        } else c._blur && (c._blur.parentNode.removeChild(c._blur), delete c._blur, delete c.attrs.blur), c.node.removeAttribute("filter")
    }, a._engine.circle = function (a, b, c, d) {
        var e = q("circle");
        a.canvas && a.canvas.appendChild(e);
        var f = new z(e, a);
        f.attrs = {cx: b, cy: c, r: d, fill: "none", stroke: "#000"}, f.type = "circle", q(e, f.attrs);
        return f
    }, a._engine.rect = function (a, b, c, d, e, f) {
        var g = q("rect");
        a.canvas && a.canvas.appendChild(g);
        var h = new z(g, a);
        h.attrs = {
            x: b,
            y: c,
            width: d,
            height: e,
            r: f || 0,
            rx: f || 0,
            ry: f || 0,
            fill: "none",
            stroke: "#000"
        }, h.type = "rect", q(g, h.attrs);
        return h
    }, a._engine.ellipse = function (a, b, c, d, e) {
        var f = q("ellipse");
        a.canvas && a.canvas.appendChild(f);
        var g = new z(f, a);
        g.attrs = {cx: b, cy: c, rx: d, ry: e, fill: "none", stroke: "#000"}, g.type = "ellipse", q(f, g.attrs);
        return g
    }, a._engine.image = function (a, b, c, d, e, f) {
        var g = q("image");
        q(g, {
            x: c,
            y: d,
            width: e,
            height: f,
            preserveAspectRatio: "none"
        }), g.setAttributeNS(n, "href", b), a.canvas && a.canvas.appendChild(g);
        var h = new z(g, a);
        h.attrs = {x: c, y: d, width: e, height: f, src: b}, h.type = "image";
        return h
    }, a._engine.text = function (b, c, d, e) {
        var f = q("text");
        b.canvas && b.canvas.appendChild(f);
        var g = new z(f, b);
        g.attrs = {
            x: c,
            y: d,
            "text-anchor": "middle",
            text: e,
            font: a._availableAttrs.font,
            stroke: "none",
            fill: "#000"
        }, g.type = "text", w(g, g.attrs);
        return g
    }, a._engine.setSize = function (a, b) {
        this.width = a || this.width, this.height = b || this.height, this.canvas.setAttribute("width", this.width), this.canvas.setAttribute("height", this.height), this._viewBox && this.setViewBox.apply(this, this._viewBox);
        return this
    }, a._engine.create = function () {
        var b = a._getContainer.apply(0, arguments), c = b && b.container, d = b.x, e = b.y, f = b.width, g = b.height;
        if (!c)throw new Error("SVG container not found.");
        var h = q("svg"), i = "overflow:hidden;", j;
        d = d || 0, e = e || 0, f = f || 512, g = g || 342, q(h, {
            height: g,
            version: 1.1,
            width: f,
            xmlns: "http://www.w3.org/2000/svg"
        }), c == 1 ? (h.style.cssText = i + "position:absolute;left:" + d + "px;top:" + e + "px", a._g.doc.body.appendChild(h), j = 1) : (h.style.cssText = i + "position:relative", c.firstChild ? c.insertBefore(h, c.firstChild) : c.appendChild(h)), c = new a._Paper, c.width = f, c.height = g, c.canvas = h, c.clear(), c._left = c._top = 0, j && (c.renderfix = function () {
        }), c.renderfix();
        return c
    }, a._engine.setViewBox = function (a, b, c, d, e) {
        k("setViewBox", this, this._viewBox, [a, b, c, d, e]);
        var f = g(c / this.width, d / this.height), h = this.top, i = e ? "meet" : "xMinYMin", j, l;
        a == null ? (this._vbSize && (f = 1), delete this._vbSize, j = "0 0 " + this.width + m + this.height) : (this._vbSize = f, j = a + m + b + m + c + m + d), q(this.canvas, {
            viewBox: j,
            preserveAspectRatio: i
        });
        while (f && h)l = "stroke-width"in h.attrs ? h.attrs["stroke-width"] : 1, h.attr({"stroke-width": l}), h._.dirty = 1, h._.dirtyT = 1, h = h.prev;
        this._viewBox = [a, b, c, d, !!e];
        return this
    }, a.prototype.renderfix = function () {
        var a = this.canvas, b = a.style, c = a.getScreenCTM() || a.createSVGMatrix(), d = -c.e % 1, e = -c.f % 1;
        if (d || e)d && (this._left = (this._left + d) % 1, b.left = this._left + "px"), e && (this._top = (this._top + e) % 1, b.top = this._top + "px")
    }, a.prototype.clear = function () {
        a.eve("clear", this);
        var b = this.canvas;
        while (b.firstChild)b.removeChild(b.firstChild);
        this.bottom = this.top = null, (this.desc = q("desc")).appendChild(a._g.doc.createTextNode("Created with Raphaël " + a.version)), b.appendChild(this.desc), b.appendChild(this.defs = q("defs"))
    }, a.prototype.remove = function () {
        k("remove", this), this.canvas.parentNode && this.canvas.parentNode.removeChild(this.canvas);
        for (var b in this)this[b] = typeof this[b] == "function" ? a._removedFactory(b) : null
    };
    var B = a.st;
    for (var C in A)A[b](C) && !B[b](C) && (B[C] = function (a) {
        return function () {
            var b = arguments;
            return this.forEach(function (c) {
                c[a].apply(c, b)
            })
        }
    }(C))
}(window.Raphael), window.Raphael.vml && function (a) {
    var b = "hasOwnProperty", c = String, d = parseFloat, e = Math, f = e.round, g = e.max, h = e.min, i = e.abs, j = "fill", k = /[, ]+/, l = a.eve, m = " progid:DXImageTransform.Microsoft", n = " ", o = "", p = {
        M: "m",
        L: "l",
        C: "c",
        Z: "x",
        m: "t",
        l: "r",
        c: "v",
        z: "x"
    }, q = /([clmz]),?([^clmz]*)/gi, r = / progid:\S+Blur\([^\)]+\)/g, s = /-?[^,\s-]+/g, t = "position:absolute;left:0;top:0;width:1px;height:1px", u = 21600, v = {
        path: 1,
        rect: 1,
        image: 1
    }, w = {circle: 1, ellipse: 1}, x = function (b) {
        var d = /[ahqstv]/ig, e = a._pathToAbsolute;
        c(b).match(d) && (e = a._path2curve), d = /[clmz]/g;
        if (e == a._pathToAbsolute && !c(b).match(d)) {
            var g = c(b).replace(q, function (a, b, c) {
                var d = [], e = b.toLowerCase() == "m", g = p[b];
                c.replace(s, function (a) {
                    e && d.length == 2 && (g += d + p[b == "m" ? "l" : "L"], d = []), d.push(f(a * u))
                });
                return g + d
            });
            return g
        }
        var h = e(b), i, j;
        g = [];
        for (var k = 0, l = h.length; k < l; k++) {
            i = h[k], j = h[k][0].toLowerCase(), j == "z" && (j = "x");
            for (var m = 1, r = i.length; m < r; m++)j += f(i[m] * u) + (m != r - 1 ? "," : o);
            g.push(j)
        }
        return g.join(n)
    }, y = function (b, c, d) {
        var e = a.matrix();
        e.rotate(-b, .5, .5);
        return {dx: e.x(c, d), dy: e.y(c, d)}
    }, z = function (a, b, c, d, e, f) {
        var g = a._, h = a.matrix, k = g.fillpos, l = a.node, m = l.style, o = 1, p = "", q, r = u / b, s = u / c;
        m.visibility = "hidden";
        if (!!b && !!c) {
            l.coordsize = i(r) + n + i(s), m.rotation = f * (b * c < 0 ? -1 : 1);
            if (f) {
                var t = y(f, d, e);
                d = t.dx, e = t.dy
            }
            b < 0 && (p += "x"), c < 0 && (p += " y") && (o = -1), m.flip = p, l.coordorigin = d * -r + n + e * -s;
            if (k || g.fillsize) {
                var v = l.getElementsByTagName(j);
                v = v && v[0], l.removeChild(v), k && (t = y(f, h.x(k[0], k[1]), h.y(k[0], k[1])), v.position = t.dx * o + n + t.dy * o), g.fillsize && (v.size = g.fillsize[0] * i(b) + n + g.fillsize[1] * i(c)), l.appendChild(v)
            }
            m.visibility = "visible"
        }
    };
    a.toString = function () {
        return "Your browser doesn’t support SVG. Falling down to VML.\nYou are running Raphaël " + this.version
    };
    var A = function (a, b, d) {
        var e = c(b).toLowerCase().split("-"), f = d ? "end" : "start", g = e.length, h = "classic", i = "medium", j = "medium";
        while (g--)switch (e[g]) {
            case"block":
            case"classic":
            case"oval":
            case"diamond":
            case"open":
            case"none":
                h = e[g];
                break;
            case"wide":
            case"narrow":
                j = e[g];
                break;
            case"long":
            case"short":
                i = e[g]
        }
        var k = a.node.getElementsByTagName("stroke")[0];
        k[f + "arrow"] = h, k[f + "arrowlength"] = i, k[f + "arrowwidth"] = j
    }, B = function (e, i) {
        e.attrs = e.attrs || {};
        var l = e.node, m = e.attrs, p = l.style, q, r = v[e.type] && (i.x != m.x || i.y != m.y || i.width != m.width || i.height != m.height || i.cx != m.cx || i.cy != m.cy || i.rx != m.rx || i.ry != m.ry || i.r != m.r), s = w[e.type] && (m.cx != i.cx || m.cy != i.cy || m.r != i.r || m.rx != i.rx || m.ry != i.ry), t = e;
        for (var y in i)i[b](y) && (m[y] = i[y]);
        r && (m.path = a._getPath[e.type](e), e._.dirty = 1), i.href && (l.href = i.href), i.title && (l.title = i.title), i.target && (l.target = i.target), i.cursor && (p.cursor = i.cursor), "blur"in i && e.blur(i.blur);
        if (i.path && e.type == "path" || r)l.path = x(~c(m.path).toLowerCase().indexOf("r") ? a._pathToAbsolute(m.path) : m.path), e.type == "image" && (e._.fillpos = [m.x, m.y], e._.fillsize = [m.width, m.height], z(e, 1, 1, 0, 0, 0));
        "transform"in i && e.transform(i.transform);
        if (s) {
            var B = +m.cx, D = +m.cy, E = +m.rx || +m.r || 0, G = +m.ry || +m.r || 0;
            l.path = a.format("ar{0},{1},{2},{3},{4},{1},{4},{1}x", f((B - E) * u), f((D - G) * u), f((B + E) * u), f((D + G) * u), f(B * u))
        }
        if ("clip-rect"in i) {
            var H = c(i["clip-rect"]).split(k);
            if (H.length == 4) {
                H[2] = +H[2] + +H[0], H[3] = +H[3] + +H[1];
                var I = l.clipRect || a._g.doc.createElement("div"), J = I.style;
                J.clip = a.format("rect({1}px {2}px {3}px {0}px)", H), l.clipRect || (J.position = "absolute", J.top = 0, J.left = 0, J.width = e.paper.width + "px", J.height = e.paper.height + "px", l.parentNode.insertBefore(I, l), I.appendChild(l), l.clipRect = I)
            }
            i["clip-rect"] || l.clipRect && (l.clipRect.style.clip = "auto")
        }
        if (e.textpath) {
            var K = e.textpath.style;
            i.font && (K.font = i.font), i["font-family"] && (K.fontFamily = '"' + i["font-family"].split(",")[0].replace(/^['"]+|['"]+$/g, o) + '"'), i["font-size"] && (K.fontSize = i["font-size"]), i["font-weight"] && (K.fontWeight = i["font-weight"]), i["font-style"] && (K.fontStyle = i["font-style"])
        }
        "arrow-start"in i && A(t, i["arrow-start"]), "arrow-end"in i && A(t, i["arrow-end"], 1);
        if (i.opacity != null || i["stroke-width"] != null || i.fill != null || i.src != null || i.stroke != null || i["stroke-width"] != null || i["stroke-opacity"] != null || i["fill-opacity"] != null || i["stroke-dasharray"] != null || i["stroke-miterlimit"] != null || i["stroke-linejoin"] != null || i["stroke-linecap"] != null) {
            var L = l.getElementsByTagName(j), M = !1;
            L = L && L[0], !L && (M = L = F(j)), e.type == "image" && i.src && (L.src = i.src), i.fill && (L.on = !0);
            if (L.on == null || i.fill == "none" || i.fill === null)L.on = !1;
            if (L.on && i.fill) {
                var N = c(i.fill).match(a._ISURL);
                if (N) {
                    L.parentNode == l && l.removeChild(L), L.rotate = !0, L.src = N[1], L.type = "tile";
                    var O = e.getBBox(1);
                    L.position = O.x + n + O.y, e._.fillpos = [O.x, O.y], a._preload(N[1], function () {
                        e._.fillsize = [this.offsetWidth, this.offsetHeight]
                    })
                } else L.color = a.getRGB(i.fill).hex, L.src = o, L.type = "solid", a.getRGB(i.fill).error && (t.type in{
                    circle: 1,
                    ellipse: 1
                } || c(i.fill).charAt() != "r") && C(t, i.fill, L) && (m.fill = "none", m.gradient = i.fill, L.rotate = !1)
            }
            if ("fill-opacity"in i || "opacity"in i) {
                var P = ((+m["fill-opacity"] + 1 || 2) - 1) * ((+m.opacity + 1 || 2) - 1) * ((+a.getRGB(i.fill).o + 1 || 2) - 1);
                P = h(g(P, 0), 1), L.opacity = P, L.src && (L.color = "none")
            }
            l.appendChild(L);
            var Q = l.getElementsByTagName("stroke") && l.getElementsByTagName("stroke")[0], T = !1;
            !Q && (T = Q = F("stroke"));
            if (i.stroke && i.stroke != "none" || i["stroke-width"] || i["stroke-opacity"] != null || i["stroke-dasharray"] || i["stroke-miterlimit"] || i["stroke-linejoin"] || i["stroke-linecap"])Q.on = !0;
            (i.stroke == "none" || i.stroke === null || Q.on == null || i.stroke == 0 || i["stroke-width"] == 0) && (Q.on = !1);
            var U = a.getRGB(i.stroke);
            Q.on && i.stroke && (Q.color = U.hex), P = ((+m["stroke-opacity"] + 1 || 2) - 1) * ((+m.opacity + 1 || 2) - 1) * ((+U.o + 1 || 2) - 1);
            var V = (d(i["stroke-width"]) || 1) * .75;
            P = h(g(P, 0), 1), i["stroke-width"] == null && (V = m["stroke-width"]), i["stroke-width"] && (Q.weight = V), V && V < 1 && (P *= V) && (Q.weight = 1), Q.opacity = P, i["stroke-linejoin"] && (Q.joinstyle = i["stroke-linejoin"] || "miter"), Q.miterlimit = i["stroke-miterlimit"] || 8, i["stroke-linecap"] && (Q.endcap = i["stroke-linecap"] == "butt" ? "flat" : i["stroke-linecap"] == "square" ? "square" : "round");
            if (i["stroke-dasharray"]) {
                var W = {
                    "-": "shortdash",
                    ".": "shortdot",
                    "-.": "shortdashdot",
                    "-..": "shortdashdotdot",
                    ". ": "dot",
                    "- ": "dash",
                    "--": "longdash",
                    "- .": "dashdot",
                    "--.": "longdashdot",
                    "--..": "longdashdotdot"
                };
                Q.dashstyle = W[b](i["stroke-dasharray"]) ? W[i["stroke-dasharray"]] : o
            }
            T && l.appendChild(Q)
        }
        if (t.type == "text") {
            t.paper.canvas.style.display = o;
            var X = t.paper.span, Y = 100, Z = m.font && m.font.match(/\d+(?:\.\d*)?(?=px)/);
            p = X.style, m.font && (p.font = m.font), m["font-family"] && (p.fontFamily = m["font-family"]), m["font-weight"] && (p.fontWeight = m["font-weight"]), m["font-style"] && (p.fontStyle = m["font-style"]), Z = d(m["font-size"] || Z && Z[0]) || 10, p.fontSize = Z * Y + "px", t.textpath.string && (X.innerHTML = c(t.textpath.string).replace(/</g, "&#60;").replace(/&/g, "&#38;").replace(/\n/g, "<br>"));
            var $ = X.getBoundingClientRect();
            t.W = m.w = ($.right - $.left) / Y, t.H = m.h = ($.bottom - $.top) / Y, t.X = m.x, t.Y = m.y + t.H / 2, ("x"in i || "y"in i) && (t.path.v = a.format("m{0},{1}l{2},{1}", f(m.x * u), f(m.y * u), f(m.x * u) + 1));
            var _ = ["x", "y", "text", "font", "font-family", "font-weight", "font-style", "font-size"];
            for (var ba = 0, bb = _.length; ba < bb; ba++)if (_[ba]in i) {
                t._.dirty = 1;
                break
            }
            switch (m["text-anchor"]) {
                case"start":
                    t.textpath.style["v-text-align"] = "left", t.bbx = t.W / 2;
                    break;
                case"end":
                    t.textpath.style["v-text-align"] = "right", t.bbx = -t.W / 2;
                    break;
                default:
                    t.textpath.style["v-text-align"] = "center", t.bbx = 0
            }
            t.textpath.style["v-text-kern"] = !0
        }
    }, C = function (b, f, g) {
        b.attrs = b.attrs || {};
        var h = b.attrs, i = Math.pow, j, k, l = "linear", m = ".5 .5";
        b.attrs.gradient = f, f = c(f).replace(a._radial_gradient, function (a, b, c) {
            l = "radial", b && c && (b = d(b), c = d(c), i(b - .5, 2) + i(c - .5, 2) > .25 && (c = e.sqrt(.25 - i(b - .5, 2)) * ((c > .5) * 2 - 1) + .5), m = b + n + c);
            return o
        }), f = f.split(/\s*\-\s*/);
        if (l == "linear") {
            var p = f.shift();
            p = -d(p);
            if (isNaN(p))return null
        }
        var q = a._parseDots(f);
        if (!q)return null;
        b = b.shape || b.node;
        if (q.length) {
            b.removeChild(g), g.on = !0, g.method = "none", g.color = q[0].color, g.color2 = q[q.length - 1].color;
            var r = [];
            for (var s = 0, t = q.length; s < t; s++)q[s].offset && r.push(q[s].offset + n + q[s].color);
            g.colors = r.length ? r.join() : "0% " + g.color, l == "radial" ? (g.type = "gradientTitle", g.focus = "100%", g.focussize = "0 0", g.focusposition = m, g.angle = 0) : (g.type = "gradient", g.angle = (270 - p) % 360), b.appendChild(g)
        }
        return 1
    }, D = function (b, c) {
        this[0] = this.node = b, b.raphael = !0, this.id = a._oid++, b.raphaelid = this.id, this.X = 0, this.Y = 0, this.attrs = {}, this.paper = c, this.matrix = a.matrix(), this._ = {
            transform: [],
            sx: 1,
            sy: 1,
            dx: 0,
            dy: 0,
            deg: 0,
            dirty: 1,
            dirtyT: 1
        }, !c.bottom && (c.bottom = this), this.prev = c.top, c.top && (c.top.next = this), c.top = this, this.next = null
    }, E = a.el;
    D.prototype = E, E.constructor = D, E.transform = function (b) {
        if (b == null)return this._.transform;
        var d = this.paper._viewBoxShift, e = d ? "s" + [d.scale, d.scale] + "-1-1t" + [d.dx, d.dy] : o, f;
        d && (f = b = c(b).replace(/\.{3}|\u2026/g, this._.transform || o)), a._extractTransform(this, e + b);
        var g = this.matrix.clone(), h = this.skew, i = this.node, j, k = ~c(this.attrs.fill).indexOf("-"), l = !c(this.attrs.fill).indexOf("url(");
        g.translate(-0.5, -0.5);
        if (l || k || this.type == "image") {
            h.matrix = "1 0 0 1", h.offset = "0 0", j = g.split();
            if (k && j.noRotation || !j.isSimple) {
                i.style.filter = g.toFilter();
                var m = this.getBBox(), p = this.getBBox(1), q = m.x - p.x, r = m.y - p.y;
                i.coordorigin = q * -u + n + r * -u, z(this, 1, 1, q, r, 0)
            } else i.style.filter = o, z(this, j.scalex, j.scaley, j.dx, j.dy, j.rotate)
        } else i.style.filter = o, h.matrix = c(g), h.offset = g.offset();
        f && (this._.transform = f);
        return this
    }, E.rotate = function (a, b, e) {
        if (this.removed)return this;
        if (a != null) {
            a = c(a).split(k), a.length - 1 && (b = d(a[1]), e = d(a[2])), a = d(a[0]), e == null && (b = e);
            if (b == null || e == null) {
                var f = this.getBBox(1);
                b = f.x + f.width / 2, e = f.y + f.height / 2
            }
            this._.dirtyT = 1, this.transform(this._.transform.concat([["r", a, b, e]]));
            return this
        }
    }, E.translate = function (a, b) {
        if (this.removed)return this;
        a = c(a).split(k), a.length - 1 && (b = d(a[1])), a = d(a[0]) || 0, b = +b || 0, this._.bbox && (this._.bbox.x += a, this._.bbox.y += b), this.transform(this._.transform.concat([["t", a, b]]));
        return this
    }, E.scale = function (a, b, e, f) {
        if (this.removed)return this;
        a = c(a).split(k), a.length - 1 && (b = d(a[1]), e = d(a[2]), f = d(a[3]), isNaN(e) && (e = null), isNaN(f) && (f = null)), a = d(a[0]), b == null && (b = a), f == null && (e = f);
        if (e == null || f == null)var g = this.getBBox(1);
        e = e == null ? g.x + g.width / 2 : e, f = f == null ? g.y + g.height / 2 : f, this.transform(this._.transform.concat([["s", a, b, e, f]])), this._.dirtyT = 1;
        return this
    }, E.hide = function () {
        !this.removed && (this.node.style.display = "none");
        return this
    }, E.show = function () {
        !this.removed && (this.node.style.display = o);
        return this
    }, E._getBBox = function () {
        if (this.removed)return {};
        return {x: this.X + (this.bbx || 0) - this.W / 2, y: this.Y - this.H, width: this.W, height: this.H}
    }, E.remove = function () {
        if (!this.removed) {
            this.paper.__set__ && this.paper.__set__.exclude(this), a.eve.unbind("*.*." + this.id), a._tear(this, this.paper), this.node.parentNode.removeChild(this.node), this.shape && this.shape.parentNode.removeChild(this.shape);
            for (var b in this)this[b] = typeof this[b] == "function" ? a._removedFactory(b) : null;
            this.removed = !0
        }
    }, E.attr = function (c, d) {
        if (this.removed)return this;
        if (c == null) {
            var e = {};
            for (var f in this.attrs)this.attrs[b](f) && (e[f] = this.attrs[f]);
            e.gradient && e.fill == "none" && (e.fill = e.gradient) && delete e.gradient, e.transform = this._.transform;
            return e
        }
        if (d == null && a.is(c, "string")) {
            if (c == j && this.attrs.fill == "none" && this.attrs.gradient)return this.attrs.gradient;
            var g = c.split(k), h = {};
            for (var i = 0, m = g.length; i < m; i++)c = g[i], c in this.attrs ? h[c] = this.attrs[c] : a.is(this.paper.customAttributes[c], "function") ? h[c] = this.paper.customAttributes[c].def : h[c] = a._availableAttrs[c];
            return m - 1 ? h : h[g[0]]
        }
        if (this.attrs && d == null && a.is(c, "array")) {
            h = {};
            for (i = 0, m = c.length; i < m; i++)h[c[i]] = this.attr(c[i]);
            return h
        }
        var n;
        d != null && (n = {}, n[c] = d), d == null && a.is(c, "object") && (n = c);
        for (var o in n)l("attr." + o + "." + this.id, this, n[o]);
        if (n) {
            for (o in this.paper.customAttributes)if (this.paper.customAttributes[b](o) && n[b](o) && a.is(this.paper.customAttributes[o], "function")) {
                var p = this.paper.customAttributes[o].apply(this, [].concat(n[o]));
                this.attrs[o] = n[o];
                for (var q in p)p[b](q) && (n[q] = p[q])
            }
            n.text && this.type == "text" && (this.textpath.string = n.text), B(this, n)
        }
        return this
    }, E.toFront = function () {
        !this.removed && this.node.parentNode.appendChild(this.node), this.paper && this.paper.top != this && a._tofront(this, this.paper);
        return this
    }, E.toBack = function () {
        if (this.removed)return this;
        this.node.parentNode.firstChild != this.node && (this.node.parentNode.insertBefore(this.node, this.node.parentNode.firstChild), a._toback(this, this.paper));
        return this
    }, E.insertAfter = function (b) {
        if (this.removed)return this;
        b.constructor == a.st.constructor && (b = b[b.length - 1]), b.node.nextSibling ? b.node.parentNode.insertBefore(this.node, b.node.nextSibling) : b.node.parentNode.appendChild(this.node), a._insertafter(this, b, this.paper);
        return this
    }, E.insertBefore = function (b) {
        if (this.removed)return this;
        b.constructor == a.st.constructor && (b = b[0]), b.node.parentNode.insertBefore(this.node, b.node), a._insertbefore(this, b, this.paper);
        return this
    }, E.blur = function (b) {
        var c = this.node.runtimeStyle, d = c.filter;
        d = d.replace(r, o), +b !== 0 ? (this.attrs.blur = b, c.filter = d + n + m + ".Blur(pixelradius=" + (+b || 1.5) + ")", c.margin = a.format("-{0}px 0 0 -{0}px", f(+b || 1.5))) : (c.filter = d, c.margin = 0, delete this.attrs.blur)
    }, a._engine.path = function (a, b) {
        var c = F("shape");
        c.style.cssText = t, c.coordsize = u + n + u, c.coordorigin = b.coordorigin;
        var d = new D(c, b), e = {fill: "none", stroke: "#000"};
        a && (e.path = a), d.type = "path", d.path = [], d.Path = o, B(d, e), b.canvas.appendChild(c);
        var f = F("skew");
        f.on = !0, c.appendChild(f), d.skew = f, d.transform(o);
        return d
    }, a._engine.rect = function (b, c, d, e, f, g) {
        var h = a._rectPath(c, d, e, f, g), i = b.path(h), j = i.attrs;
        i.X = j.x = c, i.Y = j.y = d, i.W = j.width = e, i.H = j.height = f, j.r = g, j.path = h, i.type = "rect";
        return i
    }, a._engine.ellipse = function (a, b, c, d, e) {
        var f = a.path(), g = f.attrs;
        f.X = b - d, f.Y = c - e, f.W = d * 2, f.H = e * 2, f.type = "ellipse", B(f, {cx: b, cy: c, rx: d, ry: e});
        return f
    }, a._engine.circle = function (a, b, c, d) {
        var e = a.path(), f = e.attrs;
        e.X = b - d, e.Y = c - d, e.W = e.H = d * 2, e.type = "circle", B(e, {cx: b, cy: c, r: d});
        return e
    }, a._engine.image = function (b, c, d, e, f, g) {
        var h = a._rectPath(d, e, f, g), i = b.path(h).attr({stroke: "none"}), k = i.attrs, l = i.node, m = l.getElementsByTagName(j)[0];
        k.src = c, i.X = k.x = d, i.Y = k.y = e, i.W = k.width = f, i.H = k.height = g, k.path = h, i.type = "image", m.parentNode == l && l.removeChild(m), m.rotate = !0, m.src = c, m.type = "tile", i._.fillpos = [d, e], i._.fillsize = [f, g], l.appendChild(m), z(i, 1, 1, 0, 0, 0);
        return i
    }, a._engine.text = function (b, d, e, g) {
        var h = F("shape"), i = F("path"), j = F("textpath");
        d = d || 0, e = e || 0, g = g || "", i.v = a.format("m{0},{1}l{2},{1}", f(d * u), f(e * u), f(d * u) + 1), i.textpathok = !0, j.string = c(g), j.on = !0, h.style.cssText = t, h.coordsize = u + n + u, h.coordorigin = "0 0";
        var k = new D(h, b), l = {fill: "#000", stroke: "none", font: a._availableAttrs.font, text: g};
        k.shape = h, k.path = i, k.textpath = j, k.type = "text", k.attrs.text = c(g), k.attrs.x = d, k.attrs.y = e, k.attrs.w = 1, k.attrs.h = 1, B(k, l), h.appendChild(j), h.appendChild(i), b.canvas.appendChild(h);
        var m = F("skew");
        m.on = !0, h.appendChild(m), k.skew = m, k.transform(o);
        return k
    }, a._engine.setSize = function (b, c) {
        var d = this.canvas.style;
        this.width = b, this.height = c, b == +b && (b += "px"), c == +c && (c += "px"), d.width = b, d.height = c, d.clip = "rect(0 " + b + " " + c + " 0)", this._viewBox && a._engine.setViewBox.apply(this, this._viewBox);
        return this
    }, a._engine.setViewBox = function (b, c, d, e, f) {
        a.eve("setViewBox", this, this._viewBox, [b, c, d, e, f]);
        var h = this.width, i = this.height, j = 1 / g(d / h, e / i), k, l;
        f && (k = i / e, l = h / d, d * k < h && (b -= (h - d * k) / 2 / k), e * l < i && (c -= (i - e * l) / 2 / l)), this._viewBox = [b, c, d, e, !!f], this._viewBoxShift = {
            dx: -b,
            dy: -c,
            scale: j
        }, this.forEach(function (a) {
            a.transform("...")
        });
        return this
    };
    var F;
    a._engine.initWin = function (a) {
        var b = a.document;
        b.createStyleSheet().addRule(".rvml", "behavior:url(#default#VML)");
        try {
            !b.namespaces.rvml && b.namespaces.add("rvml", "urn:schemas-microsoft-com:vml"), F = function (a) {
                return b.createElement("<rvml:" + a + ' class="rvml">')
            }
        } catch (c) {
            F = function (a) {
                return b.createElement("<" + a + ' xmlns="urn:schemas-microsoft.com:vml" class="rvml">')
            }
        }
    }, a._engine.initWin(a._g.win), a._engine.create = function () {
        var b = a._getContainer.apply(0, arguments), c = b.container, d = b.height, e, f = b.width, g = b.x, h = b.y;
        if (!c)throw new Error("VML container not found.");
        var i = new a._Paper, j = i.canvas = a._g.doc.createElement("div"), k = j.style;
        g = g || 0, h = h || 0, f = f || 512, d = d || 342, i.width = f, i.height = d, f == +f && (f += "px"), d == +d && (d += "px"), i.coordsize = u * 1e3 + n + u * 1e3, i.coordorigin = "0 0", i.span = a._g.doc.createElement("span"), i.span.style.cssText = "position:absolute;left:-9999em;top:-9999em;padding:0;margin:0;line-height:1;", j.appendChild(i.span), k.cssText = a.format("top:0;left:0;width:{0};height:{1};display:inline-block;position:relative;clip:rect(0 {0} {1} 0);overflow:hidden", f, d), c == 1 ? (a._g.doc.body.appendChild(j), k.left = g + "px", k.top = h + "px", k.position = "absolute") : c.firstChild ? c.insertBefore(j, c.firstChild) : c.appendChild(j), i.renderfix = function () {
        };
        return i
    }, a.prototype.clear = function () {
        a.eve("clear", this), this.canvas.innerHTML = o, this.span = a._g.doc.createElement("span"), this.span.style.cssText = "position:absolute;left:-9999em;top:-9999em;padding:0;margin:0;line-height:1;display:inline;", this.canvas.appendChild(this.span), this.bottom = this.top = null
    }, a.prototype.remove = function () {
        a.eve("remove", this), this.canvas.parentNode.removeChild(this.canvas);
        for (var b in this)this[b] = typeof this[b] == "function" ? a._removedFactory(b) : null;
        return !0
    };
    var G = a.st;
    for (var H in E)E[b](H) && !G[b](H) && (G[H] = function (a) {
        return function () {
            var b = arguments;
            return this.forEach(function (c) {
                c[a].apply(c, b)
            })
        }
    }(H))
}(window.Raphael)
