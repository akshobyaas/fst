{
  "version": 2,
  "buildCommand": "bash build_files.sh",
  "framework": null,
  "routes": [
    {
      "src": "/static/(.*)",
      "dest": "/static/$1"
    },
    {
      "src": "/(.*)",
      "dest": "fstp/wsgi.py"
    }
  ]
}
