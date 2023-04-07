import {Module} from '@nestjs/common';
import {AppController} from './app.controller';
import {AppService} from './app.service';
import {ServeStaticModule} from '@nestjs/serve-static';
import * as path from 'path';
import * as fs from 'fs'


console.log(path.join(__dirname, '..', 'static'))
console.log(__dirname)

@Module({
    imports: [ServeStaticModule.forRoot({
        rootPath: path.join(__dirname, '..', 'static'),
        serveRoot: '/',
        exclude: ['/api*'],
    })],
    controllers: [AppController],
    providers: [AppService],
})
export class AppModule {
}
