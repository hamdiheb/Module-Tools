import { program } from 'commander'
import fs from 'fs'
import { Buffer } from 'buffer'
import process from 'process'
program
  .command('wc <file...>')
  .description('File word counts')
  .option('-l, --line', 'print the newline counts')
  .option('-w, --count', 'print the word counts')
  .option('-c, --bytes', 'print the bytes counts')
  .action((file, options) => {
    if (file.length != 1) {
      const dir = fs.readdirSync('sample-files', { withFileTypes: true })
      dir.forEach((dirfile) => {
        const content = fs.readFileSync(`sample-files/${dirfile.name}`, 'utf-8')
        if (options.line) {
          console.log(content.split('\n').length, dirfile.name)
        }
        if (options.bytes) {
          console.log(Buffer.from(content).toString('hex'), dirfile.name)
        }
        if (options.count) {
          console.log(content.split(' ').length, dirfile.name)
        }
        if (!options.length) {
          console.log(content.split('\n').length, dirfile.name)
          console.log(Buffer.from(content).toString('hex'), dirfile.name)
          console.log(content.split(' ').length, dirfile.name)
        }
      })
    }

    if (file.length == 1) {
      const content = fs.readFileSync(`sample-files/${file}`, 'utf-8')
      if (options.line) {
        console.log(content.split('\n').length)
      }
      if (options.bytes) {
        console.log(Buffer.from(content).toString('hex'))
      }
      if (options.count) {
        console.log(content.split(' ').length)
      }
    }
  })

program.parse()
